import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPERIMENTS = [
    {
        "name": "FIRST SECURITY EXPERIMENT",
        "script": "run_first_security_experiment.py",
        "goal": "configuration drift vs surface stability",
    },
    {
        "name": "SECOND SECURITY EXPERIMENT",
        "script": "run_second_security_experiment.py",
        "goal": "log instability before visible failure",
    },
]

print("=" * 100)
print("OMNIA SECURITY — RUN ALL SECURITY EXPERIMENTS")
print("=" * 100)

successful = 0

for exp in EXPERIMENTS:

    print("\n" + "=" * 100)
    print(exp["name"])
    print("=" * 100)

    print(f"\nGOAL:\n{exp['goal']}")

    script_path = ROOT / exp["script"]

    print(f"\nSCRIPT:\n{script_path}")

    if not script_path.exists():
        print("\nSTATUS: SCRIPT NOT FOUND")
        continue

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
    )

    print("\nRETURN CODE:")
    print(result.returncode)

    print("\nSTDOUT:\n")

    if result.stdout.strip():
        print(result.stdout)
    else:
        print("(empty)")

    if result.stderr.strip():
        print("\nSTDERR:\n")
        print(result.stderr)

    if result.returncode == 0:
        successful += 1

print("\n" + "=" * 100)
print("FINAL SUMMARY")
print("=" * 100)

print(f"\nSUCCESSFUL RUNS: {successful}/{len(EXPERIMENTS)}")

if successful == len(EXPERIMENTS):
    print("\nSTATUS: ALL SECURITY EXPERIMENTS EXECUTED")
else:
    print("\nSTATUS: SOME EXPERIMENTS FAILED")

print("\nBOUNDARY:")
print("""
This repository provides:
bounded structural diagnostics
under controlled simplified conditions.

It does NOT provide:
- intrusion detection
- offensive tooling
- attack automation
- production security guarantees
""")

print("=" * 100)
print("DONE")
print("=" * 100)