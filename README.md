# OMNIA-SECURITY

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19879356.svg)](https://doi.org/10.5281/zenodo.19879356)

**OMNIA-SECURITY** is a bounded structural diagnostics repository for security-relevant behavior.

It is not a security scanner.

It is not a vulnerability scanner.

It is not exploit tooling.

It does not attack systems.

It does not exploit systems.

It does not replace security review.

Its role is narrower:

```text
measure structural drift, fragility, instability, and recoverability
in simplified security-relevant scenarios
```

Core boundary:

```text
measurement != inference != decision
```

Decision remains external.

---

## Current role

OMNIA-SECURITY applies the OMNIA measurement lineage to bounded security-relevant cases.

It focuses on post-hoc structural diagnostics:

- configuration drift
- log instability
- structural fragility
- irreversible degradation
- recoverability loss
- suspicious-clean outputs
- security-relevant structural risk signals

The repository currently contains small controlled examples, not production cybersecurity tooling.

---

## What it measures

OMNIA-SECURITY measures structural behavior such as:

- whether a system-like object remains structurally stable after perturbation
- when divergence begins
- which security-relevant properties survive transformation
- whether drift is recoverable or irreversible
- whether superficially acceptable outputs remain structurally coherent

These are structural signals.

They are not operational security decisions.

---

## What it is not

OMNIA-SECURITY is not:

- offensive tooling
- exploit generation
- malware
- vulnerability scanner
- security scanner
- penetration-testing framework
- autonomous cyber defense
- SIEM replacement
- production monitoring
- incident response system
- universal threat detector
- final decision engine

It does not exploit.

It does not attack.

It does not generate attack payloads.

It does not certify that a system is secure.

---

## Existing bounded experiments

The repository currently contains two small bounded experiments.

### Experiment 01 — Configuration drift vs surface stability

This experiment compares two simplified configurations that remain superficially operational while structurally diverging.

Core distinction:

```text
surface similarity != structural equivalence
```

Relevant files:
- [`FIRST_SECURITY_EXPERIMENT.md`](FIRST_SECURITY_EXPERIMENT.md)
- [`FIRST_SECURITY_EXPERIMENT_RESULTS.md`](FIRST_SECURITY_EXPERIMENT_RESULTS.md)
- [`COLAB_FIRST_SECURITY_RUN_V0.md`](COLAB_FIRST_SECURITY_RUN_V0.md)
- [`run_first_security_experiment.py`](run_first_security_experiment.py)

### Experiment 02 — Log instability before visible failure

This experiment compares stable and unstable authentication-like log trajectories.

Core distinction:

```text
log availability != log structural stability
```

Relevant files:
- [`SECOND_SECURITY_EXPERIMENT.md`](SECOND_SECURITY_EXPERIMENT.md)
- [`SECOND_SECURITY_EXPERIMENT_RESULTS.md`](SECOND_SECURITY_EXPERIMENT_RESULTS.md)
- [`COLAB_SECOND_SECURITY_RUN_V0.md`](COLAB_SECOND_SECURITY_RUN_V0.md)
- [`run_second_security_experiment.py`](run_second_security_experiment.py)

---

## Run

Run all current bounded examples:

```bash
python RUN_ALL_SECURITY_EXPERIMENTS.py
```

Run individual experiments:

```bash
python run_first_security_experiment.py
python run_second_security_experiment.py
```

Run repository checks:

```bash
python -m pip install -e .
python -m pytest
```

---

## Public entrypoints

- [`SECURITY_AT_A_GLANCE.md`](SECURITY_AT_A_GLANCE.md)
- [`SECURITY_CASES.md`](SECURITY_CASES.md)
- [`docs/SECURITY_SCOPE.md`](docs/SECURITY_SCOPE.md)
- [`docs/RESULTS_INDEX.md`](docs/RESULTS_INDEX.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)

---

## Methodological boundary

Correct reading:

```text
structural drift signal = diagnostic evidence
diagnostic evidence != confirmed vulnerability
confirmed vulnerability != automatic decision
measurement != inference != decision
```

Incorrect reading:

```text
OMNIA-SECURITY proves a system is secure
OMNIA-SECURITY proves a system is vulnerable
OMNIA-SECURITY replaces security review
OMNIA-SECURITY performs attacks
```

---

## Relationship to OMNIA

OMNIA-SECURITY is a verticalization of the broader OMNIA framework.

```text
OMNIA             = structural measurement core
OMNIA-SECURITY    = bounded structural diagnostics for security-relevant behavior
OMNIA-VALIDATION  = evidence / reproducibility layer
OMNIA-LIMIT       = terminal boundary layer
Decision           = external layer
```

The separation remains strict:

```text
measurement != inference != decision
```

---

## Related repositories

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- OMNIA: https://github.com/Tuttotorna/OMNIA
- OMNIA-VALIDATION: https://github.com/Tuttotorna/OMNIA-VALIDATION
- omnia-limit: https://github.com/Tuttotorna/omnia-limit
- OMNIA-RADAR: https://github.com/Tuttotorna/OMNIA-RADAR

---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19879356
https://doi.org/10.5281/zenodo.19879356
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIA-SECURITY is a bounded structural diagnostics repository.

It is not cybersecurity automation.

It is not a scanner.

It is not exploit tooling.

It measures structural behavior in security-relevant simplified cases.

Its central boundary is:

```text
measurement != inference != decision
```

---

## OMNIA-SECURITY — Public Boundary

- OMNIA-SECURITY is a bounded structural diagnostics layer for security-relevant behavior.
- OMNIA-SECURITY is not a security scanner.
- OMNIA-SECURITY is not a vulnerability scanner.
- OMNIA-SECURITY does not exploit systems.
- OMNIA-SECURITY does not attack systems.
- OMNIA-SECURITY is not a truth oracle.
- OMNIA-SECURITY is not a semantic judge.
- OMNIA-SECURITY is not a decision engine.
- measurement != inference != decision
- decision remains external

This section is a public boundary clarification. It does not change the repository core logic.\n\n- [`docs/OMNIA_SECURITY_PUBLIC_POSITION.md`](docs/OMNIA_SECURITY_PUBLIC_POSITION.md)\n\n\n## Public position

OMNIA-SECURITY public positioning is documented here:

- [`docs/OMNIA_SECURITY_PUBLIC_POSITION.md`](docs/OMNIA_SECURITY_PUBLIC_POSITION.md)

Core thesis:

```text
security signal != security proof
risk signal != final decision
```

Core boundary:

```text
security signal != safety certificate
measurement != inference != decision
```

Core role:

```text
OMNIA-SECURITY detects and organizes security-relevant structural risk signals and containment boundaries.
```

OMNIA-SECURITY does not certify safety.

It does not replace cybersecurity review.

It does not make final deployment decisions.

---
