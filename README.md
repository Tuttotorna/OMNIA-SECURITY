# OMNIA SECURITY

Structural Security Diagnostics

Part of the MB-X.01 / OMNIA structural measurement lineage.

---

# New Here

Start here:

1. [SECURITY_AT_A_GLANCE.md](./SECURITY_AT_A_GLANCE.md)
2. [SECURITY_CASES.md](./SECURITY_CASES.md)
3. [FIRST_SECURITY_EXPERIMENT.md](./FIRST_SECURITY_EXPERIMENT.md)
4. [FIRST_SECURITY_EXPERIMENT_RESULTS.md](./FIRST_SECURITY_EXPERIMENT_RESULTS.md)
5. [run_first_security_experiment.py](./run_first_security_experiment.py)

This path is currently the shortest route from first contact to the current bounded structural security direction of the repository.

---

# What It Is

OMNIA SECURITY is a bounded structural measurement layer for security-relevant systems.

It focuses on:

- instability
- drift
- irreversibility
- resilience
- divergence timing
- residual invariant integrity

under controlled transformations.

The framework is diagnostic.

It does not perform autonomous defense or offensive operations.

---

# Core Principle

```text
surface stability != structural equivalence
```

A system may appear operational while structurally diverging in security-relevant ways.

General OMNIA principle:

```text
structural truth = invariance under transformation
```

---

# Architectural Boundary

```text
measurement != inference != decision
```

OMNIA SECURITY measures structural behavior.

Interpretation and operational decisions remain external.

This repository does not collapse measurement into action.

---

# What It Measures

Current directions include:

- log instability
- configuration drift
- prompt injection structural degradation
- suspicious-clean security outputs
- resilience after perturbation
- irreversible structural loss
- residual invariant extraction
- bounded anomaly signaling

---

# First Concrete Example

The first bounded experiment compares two simplified configurations.

Baseline:

```json
{
  "auth": true,
  "tls": "enabled",
  "timeout": 30,
  "logging": "full",
  "admin_remote": false
}
```

Modified:

```json
{
  "auth": true,
  "tls": "enabled",
  "timeout": 30,
  "logging": "minimal",
  "admin_remote": true
}
```

Surface observation:

```text
both systems appear operational
both retain authentication
both retain TLS
both remain syntactically valid
```

Structural observation:

```text
logging visibility reduced
remote administrative exposure enabled
potential recoverability degradation
```

Key separation:

```text
surface similarity
!=
structural equivalence
```

Read:

- [FIRST_SECURITY_EXPERIMENT.md](./FIRST_SECURITY_EXPERIMENT.md)
- [FIRST_SECURITY_EXPERIMENT_RESULTS.md](./FIRST_SECURITY_EXPERIMENT_RESULTS.md)

Run:

```bash
python run_first_security_experiment.py
```

Runner:

- [run_first_security_experiment.py](./run_first_security_experiment.py)

---

# Example Questions

Examples of bounded questions:

```text
Does the structure remain stable after perturbation?

When does divergence begin?

Which security-relevant properties survive transformation?

Is the observed drift recoverable or irreversible?

Do superficially acceptable outputs remain structurally coherent?
```

---

# Current Security Cases

Current bounded cases are listed in:

- [SECURITY_CASES.md](./SECURITY_CASES.md)

They include:

- log instability
- configuration drift
- suspicious-clean security outputs
- irreversible structural damage
- resilience under perturbation

---

# Quick Overview

For a compressed 60-second overview, read:

- [SECURITY_AT_A_GLANCE.md](./SECURITY_AT_A_GLANCE.md)

---

# What It Is NOT

OMNIA SECURITY is NOT:

- offensive tooling
- exploit generation
- malware
- autonomous cyber defense
- attack automation
- universal threat detection
- production-grade security infrastructure

---

# Current Status

Current status:

```text
early bounded research direction
```

The repository currently defines direction, architectural scope, and a first runnable security-relevant structural drift example.

No production claims are made.

No deployment claims are made.

---

# Repository Direction

The intended direction is:

```text
security-relevant structural diagnostics
```

using the OMNIA measurement lineage:

```text
instability
drift
irreversibility
resilience
divergence timing
invariant extraction
```

---

# Relationship To OMNIA

OMNIA SECURITY is a verticalization of the broader OMNIA framework.

Core repository:

- [OMNIA](https://github.com/Tuttotorna/OMNIA)

Operational lineage:

- [lon-mirror](https://github.com/Tuttotorna/lon-mirror)

Related DOI:

- [Zenodo DOI](https://doi.org/10.5281/zenodo.19857066)

---

# Current Goal

The current goal is not universal cybersecurity.

The current goal is:

```text
bounded structural inspection
of security-relevant behavior
```

under controlled conditions.

---

# File Landmarks

Start here:

- [SECURITY_AT_A_GLANCE.md](./SECURITY_AT_A_GLANCE.md)

Cases:

- [SECURITY_CASES.md](./SECURITY_CASES.md)

First experiment:

- [FIRST_SECURITY_EXPERIMENT.md](./FIRST_SECURITY_EXPERIMENT.md)

First results:

- [FIRST_SECURITY_EXPERIMENT_RESULTS.md](./FIRST_SECURITY_EXPERIMENT_RESULTS.md)

Runner:

- [run_first_security_experiment.py](./run_first_security_experiment.py)

---

# Final Boundary

OMNIA SECURITY does not claim to secure systems.

It measures structural behavior relevant to security.

Security action remains external.