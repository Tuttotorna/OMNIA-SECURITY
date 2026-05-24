import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass(frozen=True)
class SecurityEvent:
    event_id: str
    surface: str
    content: str
    expected_boundary: str
    source: str
    target: str
    severity_hint: str
    note: str


@dataclass(frozen=True)
class SecurityAnalysis:
    event_id: str
    surface: str
    status: str
    security_score: float
    exposure_score: float
    override_score: float
    boundary_score: float
    escalation_score: float
    matched_signals: List[str]
    expected_boundary: str
    source: str
    target: str
    severity_hint: str
    note: str
    content_preview: str


EXPOSURE_PATTERNS = {
    "secret": 0.25,
    "password": 0.35,
    "api key": 0.40,
    "apikey": 0.40,
    "token": 0.30,
    "bearer": 0.35,
    "credential": 0.35,
    "private key": 0.50,
    "ssh-rsa": 0.50,
    "BEGIN PRIVATE KEY": 0.60,
    "access key": 0.45,
    "session cookie": 0.40,
    "database url": 0.35,
}

OVERRIDE_PATTERNS = {
    "ignore previous": 0.35,
    "ignore policy": 0.45,
    "bypass": 0.30,
    "jailbreak": 0.45,
    "disable safety": 0.45,
    "override instructions": 0.45,
    "developer mode": 0.35,
    "system prompt": 0.30,
    "reveal hidden": 0.35,
    "show confidential": 0.40,
    "do not refuse": 0.30,
}

BOUNDARY_PATTERNS = {
    "exfiltrate": 0.55,
    "leak": 0.35,
    "dump": 0.30,
    "unauthorized": 0.35,
    "privilege escalation": 0.55,
    "admin access": 0.40,
    "root access": 0.45,
    "delete logs": 0.45,
    "disable audit": 0.45,
    "evade detection": 0.45,
    "phishing": 0.45,
    "malware": 0.50,
    "ransomware": 0.60,
}

REGEX_SIGNALS = [
    ("email_address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), 0.15, "exposure"),
    ("ipv4_address", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), 0.12, "exposure"),
    ("long_hex_secret", re.compile(r"\b[a-fA-F0-9]{32,}\b"), 0.35, "exposure"),
    ("jwt_like_token", re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"), 0.50, "exposure"),
    ("aws_access_key_like", re.compile(r"\bAKIA[0-9A-Z]{16}\b"), 0.60, "exposure"),
    ("generic_assignment_secret", re.compile(r"\b(?:token|password|secret|apikey|api_key)\s*[:=]\s*['\"]?[^'\"\s]{6,}"), 0.45, "exposure"),
]


def normalize_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def lowercase(value: Any) -> str:
    return normalize_text(value).lower()


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def scan_dictionary(text: str, patterns: Dict[str, float], prefix: str):
    lower = text.lower()
    score = 0.0
    signals = []

    for pattern, weight in patterns.items():
        if pattern.lower() in lower:
            score += weight
            signals.append(prefix + ":" + pattern)

    return clamp01(score), signals


def scan_regex(text: str):
    exposure = 0.0
    override = 0.0
    boundary = 0.0
    signals = []

    for name, regex, weight, category in REGEX_SIGNALS:
        if regex.search(text):
            signals.append(category + ":" + name)
            if category == "exposure":
                exposure += weight
            elif category == "override":
                override += weight
            elif category == "boundary":
                boundary += weight

    return clamp01(exposure), clamp01(override), clamp01(boundary), signals


def severity_boost(severity_hint: str) -> float:
    hint = lowercase(severity_hint)

    if hint in {"critical", "blocker", "severe"}:
        return 0.25

    if hint in {"high"}:
        return 0.15

    if hint in {"medium", "moderate"}:
        return 0.08

    return 0.0


def classify_security(
    security_score: float,
    exposure_score: float,
    override_score: float,
    boundary_score: float,
    escalation_score: float,
    risk_threshold: float,
    violation_threshold: float,
    escalation_threshold: float,
) -> str:
    if escalation_score >= escalation_threshold:
        return "escalation"

    if security_score >= escalation_threshold:
        return "escalation"

    if security_score >= violation_threshold:
        return "violation"

    if security_score >= risk_threshold:
        return "risk"

    return "pass"


def analyze_event(
    event: SecurityEvent,
    risk_threshold: float = 0.20,
    violation_threshold: float = 0.45,
    escalation_threshold: float = 0.70,
) -> SecurityAnalysis:
    text = normalize_text(event.content)

    exposure_dict, exposure_signals = scan_dictionary(text, EXPOSURE_PATTERNS, "exposure")
    override_dict, override_signals = scan_dictionary(text, OVERRIDE_PATTERNS, "override")
    boundary_dict, boundary_signals = scan_dictionary(text, BOUNDARY_PATTERNS, "boundary")
    regex_exposure, regex_override, regex_boundary, regex_signals = scan_regex(text)

    exposure_score = clamp01(exposure_dict + regex_exposure)
    override_score = clamp01(override_dict + regex_override)
    boundary_score = clamp01(boundary_dict + regex_boundary)

    boost = severity_boost(event.severity_hint)

    chained_pressure = 0.0
    if exposure_score >= 0.30 and override_score >= 0.30:
        chained_pressure += 0.20
    if boundary_score >= 0.35 and override_score >= 0.30:
        chained_pressure += 0.20
    if exposure_score >= 0.40 and boundary_score >= 0.35:
        chained_pressure += 0.20

    escalation_score = clamp01(max(exposure_score, override_score, boundary_score) + chained_pressure + boost)

    security_score = clamp01(
        (0.35 * exposure_score)
        + (0.30 * override_score)
        + (0.25 * boundary_score)
        + (0.10 * escalation_score)
        + boost
    )

    matched_signals = exposure_signals + override_signals + boundary_signals + regex_signals

    if boost > 0:
        matched_signals.append("severity_hint:" + event.severity_hint)

    status = classify_security(
        security_score=security_score,
        exposure_score=exposure_score,
        override_score=override_score,
        boundary_score=boundary_score,
        escalation_score=escalation_score,
        risk_threshold=risk_threshold,
        violation_threshold=violation_threshold,
        escalation_threshold=escalation_threshold,
    )

    preview = text[:180]
    if len(text) > 180:
        preview += "..."

    return SecurityAnalysis(
        event_id=event.event_id,
        surface=event.surface,
        status=status,
        security_score=round(security_score, 12),
        exposure_score=round(exposure_score, 12),
        override_score=round(override_score, 12),
        boundary_score=round(boundary_score, 12),
        escalation_score=round(escalation_score, 12),
        matched_signals=matched_signals,
        expected_boundary=event.expected_boundary,
        source=event.source,
        target=event.target,
        severity_hint=event.severity_hint,
        note=event.note,
        content_preview=preview,
    )


def read_jsonl(path: str) -> List[SecurityEvent]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)

    events = []

    with p.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw:
                continue

            try:
                obj = json.loads(raw)
            except json.JSONDecodeError as e:
                raise ValueError("Invalid JSONL at line " + str(line_no) + ": " + str(e))

            for field in ["event_id", "surface", "content"]:
                if field not in obj:
                    raise ValueError("Missing required field '" + field + "' at line " + str(line_no))

            events.append(
                SecurityEvent(
                    event_id=str(obj["event_id"]),
                    surface=str(obj["surface"]),
                    content=str(obj["content"]),
                    expected_boundary=str(obj.get("expected_boundary", "")),
                    source=str(obj.get("source", "")),
                    target=str(obj.get("target", "")),
                    severity_hint=str(obj.get("severity_hint", "")),
                    note=str(obj.get("note", "")),
                )
            )

    if not events:
        raise ValueError("No events found in " + path)

    seen = set()
    for event in events:
        if event.event_id in seen:
            raise ValueError("Duplicate event_id: " + event.event_id)
        seen.add(event.event_id)

    return events


def analyze_events(
    events: List[SecurityEvent],
    risk_threshold: float = 0.20,
    violation_threshold: float = 0.45,
    escalation_threshold: float = 0.70,
) -> Dict[str, Any]:
    analyses = [
        analyze_event(
            event=e,
            risk_threshold=risk_threshold,
            violation_threshold=violation_threshold,
            escalation_threshold=escalation_threshold,
        )
        for e in events
    ]

    rows = [asdict(a) for a in analyses]

    pass_rows = [r for r in rows if r["status"] == "pass"]
    risk_rows = [r for r in rows if r["status"] == "risk"]
    violation_rows = [r for r in rows if r["status"] == "violation"]
    escalation_rows = [r for r in rows if r["status"] == "escalation"]

    total_events = len(rows)
    worst = max(rows, key=lambda r: r["security_score"]) if rows else None

    summary = {
        "total_events": total_events,
        "pass": len(pass_rows),
        "risk": len(risk_rows),
        "violation": len(violation_rows),
        "escalation": len(escalation_rows),
        "pass_rate": round(len(pass_rows) / total_events, 12) if total_events else 0.0,
        "risk_rate": round(len(risk_rows) / total_events, 12) if total_events else 0.0,
        "violation_rate": round(len(violation_rows) / total_events, 12) if total_events else 0.0,
        "escalation_rate": round(len(escalation_rows) / total_events, 12) if total_events else 0.0,
        "max_security_score": worst["security_score"] if worst else None,
        "worst_event_id": worst["event_id"] if worst else None,
        "problem_solved": "Measures structural security risk, violation, and escalation states inside supplied events.",
    }

    certificate = {
        "audit_type": "omnia_security_audit",
        "summary": summary,
        "thresholds": {
            "risk_threshold": risk_threshold,
            "violation_threshold": violation_threshold,
            "escalation_threshold": escalation_threshold,
        },
        "boundary": "measurement only; security status means structural risk inside supplied events, not legal, semantic, or operational final judgment",
        "measurement_language": [
            "event_id",
            "surface",
            "exposure_score",
            "override_score",
            "boundary_score",
            "escalation_score",
            "security_score",
            "pass_risk_violation_escalation",
        ],
    }

    return {
        "summary": summary,
        "thresholds": {
            "risk_threshold": risk_threshold,
            "violation_threshold": violation_threshold,
            "escalation_threshold": escalation_threshold,
        },
        "certificate": certificate,
        "events": rows,
    }


def write_json(path: str, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "event_id",
        "surface",
        "status",
        "security_score",
        "exposure_score",
        "override_score",
        "boundary_score",
        "escalation_score",
        "matched_signals",
        "expected_boundary",
        "source",
        "target",
        "severity_hint",
        "note",
        "content_preview",
    ]

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for row in result["events"]:
            out = dict(row)
            out["matched_signals"] = " | ".join(row.get("matched_signals", []))
            writer.writerow({k: out.get(k, "") for k in fields})


def html_escape(x: Any) -> str:
    return str(x).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_html_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    summary = result["summary"]

    rows = []
    for r in result["events"]:
        if r["status"] == "pass":
            continue

        rows.append(
            "<tr>"
            + "<td>" + html_escape(r["event_id"]) + "</td>"
            + "<td>" + html_escape(r["surface"]) + "</td>"
            + "<td>" + html_escape(r["status"]) + "</td>"
            + "<td>" + html_escape(r["security_score"]) + "</td>"
            + "<td>" + html_escape(r["exposure_score"]) + "</td>"
            + "<td>" + html_escape(r["override_score"]) + "</td>"
            + "<td>" + html_escape(r["boundary_score"]) + "</td>"
            + "<td>" + html_escape(r["escalation_score"]) + "</td>"
            + "<td>" + html_escape(" | ".join(r["matched_signals"])) + "</td>"
            + "<td>" + html_escape(r["content_preview"]) + "</td>"
            + "</tr>"
        )

    html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>OMNIA Security Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 32px;
      line-height: 1.45;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background: #f2f2f2;
    }}
    .box {{
      background: #f8f8f8;
      padding: 16px;
      margin-bottom: 24px;
      border: 1px solid #eee;
    }}
  </style>
</head>
<body>
  <h1>OMNIA Security Report</h1>

  <div class="box">
    <p><b>Total events:</b> {total_events}</p>
    <p><b>Pass:</b> {pass_count}</p>
    <p><b>Risk:</b> {risk}</p>
    <p><b>Violation:</b> {violation}</p>
    <p><b>Escalation:</b> {escalation}</p>
    <p><b>Max security score:</b> {max_security_score}</p>
    <p><b>Worst event:</b> {worst_event_id}</p>
  </div>

  <h2>Risk / Violation / Escalation Events</h2>

  <table>
    <tr>
      <th>Event</th>
      <th>Surface</th>
      <th>Status</th>
      <th>Security</th>
      <th>Exposure</th>
      <th>Override</th>
      <th>Boundary</th>
      <th>Escalation</th>
      <th>Signals</th>
      <th>Preview</th>
    </tr>
    {rows}
  </table>

  <h2>Boundary</h2>
  <p>Security status means structural risk inside supplied events. This is not legal, semantic, or operational final judgment.</p>
</body>
</html>
""".format(
        total_events=summary["total_events"],
        pass_count=summary["pass"],
        risk=summary["risk"],
        violation=summary["violation"],
        escalation=summary["escalation"],
        max_security_score=summary["max_security_score"],
        worst_event_id=summary["worst_event_id"],
        rows="".join(rows),
    )

    p.write_text(html, encoding="utf-8")


def write_event_jsonl(path: str, result: Dict[str, Any], status: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", encoding="utf-8") as f:
        for r in result["events"]:
            if r["status"] == status:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_all_reports(out_dir: str, result: Dict[str, Any]) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    write_json(str(out / "report.json"), result)
    write_csv_report(str(out / "report.csv"), result)
    write_html_report(str(out / "report.html"), result)
    write_event_jsonl(str(out / "risk_events.jsonl"), result, "risk")
    write_event_jsonl(str(out / "violation_events.jsonl"), result, "violation")
    write_event_jsonl(str(out / "escalation_events.jsonl"), result, "escalation")
    write_json(str(out / "certificate.json"), result["certificate"])
