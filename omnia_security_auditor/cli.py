import argparse
import sys
from pathlib import Path

from .core import analyze_events, read_jsonl, write_all_reports


def main():
    parser = argparse.ArgumentParser(
        prog="omnia-security-audit",
        description="Audit structural security risk, violation, and escalation inside supplied events.",
    )

    parser.add_argument("--input", required=True, help="JSONL file with event_id, surface, and content.")
    parser.add_argument("--out-dir", default="omnia_security_report", help="Output directory.")
    parser.add_argument("--risk-threshold", type=float, default=0.20, help="Security score threshold above which an event is risk.")
    parser.add_argument("--violation-threshold", type=float, default=0.45, help="Security score threshold above which an event is violation.")
    parser.add_argument("--escalation-threshold", type=float, default=0.70, help="Security or escalation score threshold above which an event is escalation.")
    parser.add_argument("--fail-on-violation", action="store_true", help="Exit with code 2 if violation appears, or 3 if escalation appears.")
    parser.add_argument("--fail-on-escalation", action="store_true", help="Exit with code 3 if escalation appears.")

    args = parser.parse_args()

    try:
        events = read_jsonl(args.input)
        result = analyze_events(
            events=events,
            risk_threshold=args.risk_threshold,
            violation_threshold=args.violation_threshold,
            escalation_threshold=args.escalation_threshold,
        )
        write_all_reports(args.out_dir, result)
    except Exception as e:
        print("ERROR:", str(e))
        sys.exit(4)

    s = result["summary"]

    print("")
    print("OMNIA SECURITY AUDIT")
    print("====================")
    print(f"input:               {args.input}")
    print(f"total_events:        {s['total_events']}")
    print(f"pass:                {s['pass']}")
    print(f"risk:                {s['risk']}")
    print(f"violation:           {s['violation']}")
    print(f"escalation:          {s['escalation']}")
    print(f"pass_rate:           {s['pass_rate']:.6f}")
    print(f"risk_rate:           {s['risk_rate']:.6f}")
    print(f"violation_rate:      {s['violation_rate']:.6f}")
    print(f"escalation_rate:     {s['escalation_rate']:.6f}")
    print(f"max_security_score:  {s['max_security_score']}")
    print(f"worst_event_id:      {s['worst_event_id']}")
    print("")
    print(f"WROTE: {Path(args.out_dir) / 'report.json'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.csv'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.html'}")
    print(f"WROTE: {Path(args.out_dir) / 'risk_events.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'violation_events.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'escalation_events.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'certificate.json'}")
    print("")

    if args.fail_on_escalation and s["escalation"] > 0:
        sys.exit(3)

    if args.fail_on_violation:
        if s["escalation"] > 0:
            sys.exit(3)
        if s["violation"] > 0:
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
