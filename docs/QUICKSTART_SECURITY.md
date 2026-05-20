# Quickstart Security

This document gives the fastest path to seeing OMNIA-SECURITY as bounded structural diagnostics for security-relevant traces.

The public mental model is:

    security-relevant trace -> structural diagnostic -> risk signal -> external security decision

---

## Clean install

    git clone https://github.com/Tuttotorna/OMNIA-SECURITY.git
    cd OMNIA-SECURITY
    python -m pip install -e .
    pytest

---

## What to look for

After installation and tests, look for the smallest available example.

The point is not to scan systems.

The point is to identify:

    What security-relevant trace is being diagnosed?
    What structural diagnostic is applied?
    What signal appears?
    Is the signal bounded?
    What report is produced?
    What remains external?

---

## Expected diagnostic behavior

A good OMNIA-SECURITY path should produce a bounded diagnostic artifact.

It should not silently become:

    scanner output
    exploit instruction
    vulnerability verdict
    final security decision
    semantic truth certificate

---

## Public compression

    OMNIA-SECURITY diagnoses structural behavior.
    It is not a security scanner.
    It is not a vulnerability scanner.
    It does not attack.
    It does not exploit.
    It is not a verdict engine.
    Decision remains external.

