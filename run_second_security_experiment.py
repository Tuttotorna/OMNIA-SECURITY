from collections import Counter

print("=" * 100)
print("OMNIA SECURITY — SECOND SECURITY EXPERIMENT")
print("=" * 100)

stable_logs = [
    "auth_success user=alice method=password",
    "auth_success user=bob method=password",
    "auth_success user=carol method=password",
    "auth_success user=dave method=password",
    "auth_success user=erin method=password",
]

unstable_logs = [
    "auth_success user=alice method=password",
    "auth_retry user=alice method=password",
    "auth_retry user=alice method=password",
    "auth_error user=unknown method=missing",
    "auth_bypass_attempt user=unknown method=null",
]

print("\n" + "=" * 100)
print("STABLE TRAJECTORY")
print("=" * 100)

for i, log in enumerate(stable_logs, start=1):
    print(f"t{i}: {log}")

print("\n" + "=" * 100)
print("UNSTABLE TRAJECTORY")
print("=" * 100)

for i, log in enumerate(unstable_logs, start=1):
    print(f"t{i}: {log}")


def extract_event(log):
    return log.split()[0]


def trajectory_metrics(logs):
    events = [extract_event(x) for x in logs]

    unique_ratio = len(set(events)) / len(events)

    repetition_ratio = max(Counter(events).values()) / len(events)

    instability = unique_ratio + repetition_ratio

    return {
        "events": events,
        "unique_ratio": unique_ratio,
        "repetition_ratio": repetition_ratio,
        "instability": instability,
    }


stable = trajectory_metrics(stable_logs)
unstable = trajectory_metrics(unstable_logs)

print("\n" + "=" * 100)
print("SURFACE OBSERVATION")
print("=" * 100)

print("""
Both trajectories remain:

- parseable
- syntactically valid
- authentication-related
- operationally active
""")

print("\nSurface interpretation:")
print("Both systems continue emitting logs.")

print("\n" + "=" * 100)
print("STRUCTURAL OBSERVATION")
print("=" * 100)

print("\nStable events:")
print(stable["events"])

print("\nUnstable events:")
print(unstable["events"])

print("\nStable trajectory metrics:")
print(f"Unique ratio:      {stable['unique_ratio']:.2f}")
print(f"Repetition ratio:  {stable['repetition_ratio']:.2f}")

print("\nUnstable trajectory metrics:")
print(f"Unique ratio:      {unstable['unique_ratio']:.2f}")
print(f"Repetition ratio:  {unstable['repetition_ratio']:.2f}")

print("\nIllustrative structural interpretation:\n")

stable_sei = 0.95
stable_tdelta = "late / undefined"

unstable_sei = 0.45
unstable_tdelta = "early"

print("Stable trajectory:")
print(f"SEI (illustrative):      {stable_sei}")
print(f"TDelta (illustrative):   {stable_tdelta}")

print("\nUnstable trajectory:")
print(f"SEI (illustrative):      {unstable_sei}")
print(f"TDelta (illustrative):   {unstable_tdelta}")

print("\nObserved drift accumulation:")

drift_signals = [
    "retry concentration",
    "event taxonomy drift",
    "unknown identity emergence",
    "field degradation",
]

for signal in drift_signals:
    print(f"- {signal}")

print("\nInterpretation:")
print("Structural instability increases before visible failure.")

print("\n" + "=" * 100)
print("KEY SEPARATION")
print("=" * 100)

print("""
log availability
!=
log structural stability
""")

print("\n" + "=" * 100)
print("BOUNDARY")
print("=" * 100)

print("""
This experiment is illustrative only.

It does NOT perform:
- intrusion detection
- attack attribution
- threat classification
- production telemetry analysis

It demonstrates only:
bounded structural diagnostics
for log instability.
""")

print("=" * 100)
print("DONE")
print("=" * 100)