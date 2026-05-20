# Not a Scanner, Not a Verdict

This document states the negative boundary explicitly.

OMNIA-SECURITY is not a security scanner.

OMNIA-SECURITY is not a vulnerability scanner.

OMNIA-SECURITY is not an exploit tool.

OMNIA-SECURITY is not a vulnerability verdict engine.

OMNIA-SECURITY does not attack.

OMNIA-SECURITY does not exploit.

---

## Why this matters

Security language is high-stakes.

A diagnostic signal can easily be misread as a confirmed vulnerability or exploit path.

This repository must prevent that confusion.

Its role is bounded diagnosis:

    security-relevant trace -> structural diagnostic -> risk signal -> external review

---

## What OMNIA-SECURITY may do

OMNIA-SECURITY may:

- inspect security-relevant traces;
- emit bounded structural diagnostics;
- flag risk signals;
- generate reports;
- route artifacts to validation;
- require external security review.

---

## What OMNIA-SECURITY may not claim

OMNIA-SECURITY should not claim:

- confirmed vulnerability;
- exploitability;
- system compromise;
- security verdict;
- attack instructions;
- final decision authority.

---

## Boundary phrase

    diagnostic != exploit
    risk signal != vulnerability verdict
    not a security scanner
    not a vulnerability scanner
    does not attack
    does not exploit
    measurement != inference != decision
    Decision remains external

