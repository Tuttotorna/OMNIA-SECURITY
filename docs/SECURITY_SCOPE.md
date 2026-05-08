# OMNIA-SECURITY Scope

## Purpose

OMNIA-SECURITY is a bounded structural diagnostics layer for security-relevant behavior.

It measures structural drift, fragility, instability, and recoverability loss in simplified controlled cases.

## Boundary

```text
measurement != inference != decision
diagnostic signal != confirmed vulnerability
structural drift != exploit
security-relevant measurement != security scanner
```

## What is in scope

OMNIA-SECURITY may measure:

- configuration drift
- log instability
- structural fragility
- security-relevant degradation
- irreversibility
- resilience after perturbation
- suspicious-clean structural behavior
- recoverability loss

## What is out of scope

OMNIA-SECURITY does not perform:

- exploitation
- attack automation
- vulnerability scanning
- penetration testing
- malware analysis as an operational tool
- credential discovery
- payload generation
- incident response
- production monitoring
- security certification

## Correct interpretation

```text
signal = structural diagnostic evidence
evidence = input to external review
external review = outside this repository
decision remains external
```
