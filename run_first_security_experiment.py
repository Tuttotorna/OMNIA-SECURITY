import json

print("=" * 100)
print("OMNIA SECURITY — FIRST SECURITY EXPERIMENT")
print("=" * 100)

baseline = {
    "auth": True,
    "tls": "enabled",
    "timeout": 30,
    "logging": "full",
    "admin_remote": False,
}

modified = {
    "auth": True,
    "tls": "enabled",
    "timeout": 30,
    "logging": "minimal",
    "admin_remote": True,
}

print("\nBASELINE CONFIGURATION\n")
print(json.dumps(baseline, indent=2))

print("\nMODIFIED CONFIGURATION\n")
print(json.dumps(modified, indent=2))

shared_keys = []
changed_keys = []

for key in baseline:
    if baseline[key] == modified[key]:
        shared_keys.append(key)
    else:
        changed_keys.append(key)

surface_similarity = len(shared_keys) / len(baseline)

print("\n" + "=" * 100)
print("SURFACE OBSERVATION")
print("=" * 100)

print(f"\nShared fields: {shared_keys}")
print(f"Changed fields: {changed_keys}")

print(f"\nSurface similarity: {surface_similarity:.2f}")

if surface_similarity >= 0.6:
    print("\nSurface interpretation:")
    print("Configurations appear superficially similar.")
else:
    print("\nSurface interpretation:")
    print("Configurations visibly diverge.")

print("\n" + "=" * 100)
print("STRUCTURAL OBSERVATION")
print("=" * 100)

structural_flags = []

if baseline["logging"] != modified["logging"]:
    structural_flags.append(
        "logging visibility reduced"
    )

if baseline["admin_remote"] != modified["admin_remote"]:
    structural_flags.append(
        "remote administrative exposure enabled"
    )

for flag in structural_flags:
    print(f"- {flag}")

print("\nIllustrative structural interpretation:\n")

omega = 1.00 - (0.15 * len(structural_flags))
compatibility = 1.00 - (0.20 * len(structural_flags))

print(f"Omega (illustrative):        {omega:.2f}")
print(f"Compatibility (illustrative): {compatibility:.2f}")

if len(structural_flags) > 0:
    print("\nPotential structural drift detected.")
else:
    print("\nNo structural drift detected.")

print("\n" + "=" * 100)
print("BOUNDARY")
print("=" * 100)

print("""
This experiment is illustrative only.

It does NOT perform:
- intrusion detection
- vulnerability scanning
- production security analysis

It demonstrates only:
bounded structural diagnostics
for security-relevant drift.
""")

print("=" * 100)
print("DONE")
print("=" * 100)