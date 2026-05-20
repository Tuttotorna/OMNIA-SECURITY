# Diagnostic Contract

This document defines the public shape expected from OMNIA-SECURITY diagnostic results.

The goal is clarity.

A reviewer should understand what trace was diagnosed, what signal appeared, and what the result does not prove.

---

## Diagnostic unit

A security diagnostic result should contain:

| Component | Required | Meaning |
|---|---:|---|
| case_id | yes | Stable identifier for the diagnostic case |
| trace_ref | yes | Security-relevant trace or artifact |
| diagnostic_mode | yes | Declared diagnostic method |
| structural_signal | preferred | Detected or measured structural signal |
| risk_signal | yes | no_signal, risk_signal, anomaly, unstable, candidate, or inconclusive |
| report_ref | preferred | Report or artifact path |
| limitation | yes | What the diagnostic does not prove |
| external_review | yes | Explicit statement that security decision remains external |

---

## Minimal JSON shape

A minimal diagnostic artifact can use this shape:

    {{
      "case_id": "security-example-001",
      "trace_ref": "path-or-description",
      "diagnostic_mode": "declared structural diagnostic",
      "structural_signal": "declared signal or null",
      "risk_signal": "no_signal | risk_signal | anomaly | unstable | candidate | inconclusive",
      "boundary": "measurement != inference != decision",
      "limitation": "What this diagnostic does not prove",
      "external_review": "Security decision remains external"
    }}

---

## Result vocabulary

Use a small vocabulary:

    no_signal
    risk_signal
    anomaly
    unstable
    candidate
    inconclusive

Meaning:

- no_signal: no relevant structural signal found;
- risk_signal: bounded signal requiring external review;
- anomaly: unexpected structural behavior;
- unstable: structural instability appears;
- candidate: result should be tested further;
- inconclusive: evidence is insufficient.

---

## No silent promotion

A diagnostic result must not silently become a vulnerability verdict.

A risk signal is not proof of exploitability.

An anomaly is not a confirmed vulnerability.

A bounded report is not a final security decision.

