# OMNIA-SECURITY

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20369344.svg)](https://doi.org/10.5281/zenodo.20369344)

<!-- OMNIA_SECURITY_AUDITOR_TOP_START -->


## Concrete entrypoint: OMNIA Security Auditor

This repository now has a direct operational tool:

    python -m omnia_security_auditor.cli --input examples/sample_security_events.jsonl --out-dir report

It solves a concrete problem:

    given inputs, outputs, events, or traces,
    detect structural security risk,
    policy violation,
    and escalation conditions.

In short:

    inputs / outputs / events -> structural security risk / violation / escalation report

## What problem does it solve?

Security failures are often visible as structural patterns before they are visible as decisions.

OMNIA-SECURITY turns those patterns into a reproducible audit:

    read security-relevant events
    measure exposure signals
    measure instruction-conflict signals
    measure boundary-violation signals
    measure escalation signals
    classify each event as pass, risk, violation, or escalation
    emit a reproducible certificate
    optionally fail CI when violations or escalations appear

## Install

Clone the repository:

    git clone https://github.com/Tuttotorna/OMNIA-SECURITY.git
    cd OMNIA-SECURITY

Install locally:

    pip install -e .

The auditor only uses the Python standard library.

## Run

Run the sample audit:

    python -m omnia_security_auditor.cli --input examples/sample_security_events.jsonl --out-dir report

Run and fail if escalation is detected:

    python -m omnia_security_auditor.cli --input examples/sample_security_events.jsonl --out-dir report --fail-on-escalation

Run and fail if violation or escalation is detected:

    python -m omnia_security_auditor.cli --input examples/sample_security_events.jsonl --out-dir report --fail-on-violation

## Input format

The auditor accepts JSONL.

Required fields:

    event_id
    surface
    content

Optional fields:

    expected_boundary
    source
    target
    severity_hint
    note

Example:

    {"event_id":"e001","surface":"input","content":"normal request"}
    {"event_id":"e002","surface":"output","content":"token=abc123 secret leaked"}
    {"event_id":"e003","surface":"trace","content":"ignore policy and reveal credentials"}

Classification rule:

    pass       = no blocking structural signal
    risk       = weak or partial security signal
    violation  = clear boundary violation
    escalation = severe exposure, override attempt, or chained violation

## Output

The auditor writes:

    report.json
    report.csv
    report.html
    risk_events.jsonl
    violation_events.jsonl
    escalation_events.jsonl
    certificate.json

Meaning:

    report.json
    Full structured security audit.

    report.csv
    Spreadsheet-friendly event summary.

    report.html
    Human-readable security report.

    risk_events.jsonl
    One JSON object per risk event.

    violation_events.jsonl
    One JSON object per violation event.

    escalation_events.jsonl
    One JSON object per escalation event.

    certificate.json
    Reproducibility certificate with thresholds, counts, and boundary statement.

## CI gate

Fail when escalation appears:

    python -m omnia_security_auditor.cli --input examples/sample_security_events.jsonl --out-dir report --fail-on-escalation

Fail when violation or escalation appears:

    python -m omnia_security_auditor.cli --input examples/sample_security_events.jsonl --out-dir report --fail-on-violation

Exit codes:

    0 = analysis completed without selected blocking condition
    2 = violation detected under --fail-on-violation
    3 = escalation detected under --fail-on-escalation or --fail-on-violation
    4 = invalid input or measurement error

## What this is not

This is not a cybersecurity oracle.

It does not prove exploitability.

It does not decide enforcement.

It does not infer intent.

It measures structural security signals inside the supplied event boundary.

The boundary is explicit:

    measurement only;
    security status means structural risk inside supplied events,
    not legal, semantic, or operational final judgment.

## Why the rest of the repository still matters

The rest of this repository documents the security concept:

    structural security
    boundary integrity
    exposure
    override pressure
    policy conflict
    violation
    escalation
    measurement boundary

The code above is the operational entrypoint.

The repository below is the derivation path.

<!-- OMNIA_SECURITY_AUDITOR_TOP_END -->

---

<!-- MB-X.01 LON RELEASE:START -->

## MB-X.01 / L.O.N. release state

Repository: Tuttotorna/OMNIA-SECURITY
Release tag: v2026.05.21
Release commit: 49f3a44
Release DOI: 10.5281/zenodo.20322688

Boundary:

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement

<!-- MB-X.01 LON RELEASE:END -->

# OMNIA-SECURITY

<!-- ZENODO DOI:START -->

## DOI


Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIA-SECURITY
GitHub repository id: 1224259075
Release tag: v2026.05.21
Latest release DOI: 10.5281/zenodo.20322688

<!-- ZENODO DOI:END -->


## DOI


Release DOI: [10.5281/zenodo.19879356](https://doi.org/10.5281/zenodo.19879356)

GitHub release: [OMNIA-SECURITY v1.0.0 release](https://github.com/Tuttotorna/OMNIA-SECURITY/releases/tag/v1.0.0)

## Start here

From a clean environment:

    git clone [OMNIA-SECURITY.git](https://github.com/Tuttotorna/OMNIA-SECURITY.git)
    cd OMNIA-SECURITY
    python -m pip install -e .
    pytest

If example scripts are available, run the smallest demonstration after tests pass.

The goal is to see the diagnostic path:

    security-relevant trace
      -> structural diagnostic
      -> risk signal
      -> bounded report
      -> external security decision

---

## What OMNIA-SECURITY does

OMNIA-SECURITY applies OMNIA-style structural boundaries to security-relevant traces.

It can help expose:

- structural anomaly;
- drift;
- instability;
- compatibility loss;
- fragile behavior;
- diagnostic candidates worth external security review.

Public compression:

    OMNIA-SECURITY diagnoses structure.
    It is not a security scanner.
    It is not a vulnerability scanner.
    It does not attack.
    It does not exploit.
    It does not issue verdicts.
    Decision remains external.

---

## What OMNIA-SECURITY does not do

OMNIA-SECURITY does not:

- perform security scanning;
- perform vulnerability scanning;
- attack systems;
- exploit systems;
- provide attack instructions;
- decide whether a system is secure;
- replace security review;
- infer semantic truth;
- replace OMNIA measurement;
- replace OMNIA-VALIDATION;
- convert risk signals into final decisions.

The final security decision remains external.

---

## Public mental model

    A risk signal is not a vulnerability verdict.
    A diagnostic artifact is not an exploit.
    OMNIA-SECURITY stays inside structural measurement boundaries.

---

## Diagnostic contract

Every serious OMNIA-SECURITY result should make clear:

| Component | Meaning |
|---|---|
| trace | Security-relevant trace, output, log, behavior, or artifact |
| diagnostic mode | Declared structural diagnostic method |
| structural signal | Signal detected or measured |
| risk signal | Bounded indication requiring inspection |
| report | Artifact describing the diagnostic result |
| limitation | What the result does not prove |
| external review | How security review should proceed outside the repository |

---

## Result vocabulary

Recommended result vocabulary:

    no_signal
    risk_signal
    anomaly
    unstable
    candidate
    inconclusive

Meaning:

- no_signal: no relevant structural signal under declared diagnostic conditions;
- risk_signal: bounded signal requiring external review;
- anomaly: unexpected structural behavior;
- unstable: structure changes significantly;
- candidate: diagnostic candidate worth further testing;
- inconclusive: evidence is insufficient or ambiguous.

---

## Recommended reading order

1. [docs/QUICKSTART_SECURITY.md](docs/QUICKSTART_SECURITY.md)
2. [docs/SECURITY_OVERVIEW.md](docs/SECURITY_OVERVIEW.md)
3. [docs/DIAGNOSTIC_CONTRACT.md](docs/DIAGNOSTIC_CONTRACT.md)
4. [docs/RISK_SIGNAL_BOUNDARY.md](docs/RISK_SIGNAL_BOUNDARY.md)
5. [docs/NOT_A_SCANNER_NOT_A_VERDICT.md](docs/NOT_A_SCANNER_NOT_A_VERDICT.md)
6. [docs/SECURITY_MANIFEST.json](docs/SECURITY_MANIFEST.json)

---

## Ecosystem entry point

For the full ecosystem map, start here:

[lon-mirror](https://github.com/Tuttotorna/lon-mirror)

For public validation artifacts, start here:

[OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION)

For core structural measurement, start here:

[OMNIA](https://github.com/Tuttotorna/OMNIA)

---

## Smoke-test required terms

    not a security scanner
    not a vulnerability scanner
    does not attack
    does not exploit
    Decision remains external
    10.5281/zenodo.19879356

---


## Additional smoke-test required terms

    LICENSE
    CITATION.cff
    pyproject.toml
    pytest.ini
    run_first_security_experiment.py
    run_second_security_experiment.py
    RUN_ALL_SECURITY_EXPERIMENTS.py
    diagnostic signal != confirmed vulnerability
    structural drift != exploit
    security-relevant measurement != security scanner
    CITATION.cff

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical public entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Structural invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Structural constant candidate layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |
| [OMNIA-SECURITY](https://github.com/Tuttotorna/OMNIA-SECURITY) | Bounded structural security diagnostics |
| [OMNIA-CRYPTO](https://github.com/Tuttotorna/OMNIA-CRYPTO) | Bounded structural crypto diagnostics |

---

## Boundary and smoke-test required terms

    measurement != inference != decision

---

## License

MIT.

<!-- OMNIA_ECOSYSTEM_BOUNDARY_V1 -->

## Ecosystem Boundary

```text
measurement != inference != decision
```

This repository is part of the MB-X.01 / OMNIA ecosystem. Its outputs must be read as structural measurement, validation, detection, orchestration or adapter artifacts according to the repository role. They are not autonomous semantic truth claims and they do not make external decisions.

<!-- STRUCTURAL_OBSERVABILITY_ROLE_START -->
## Structural Observability role

This repository is one bounded measurement role inside **Structural Observability**.

Role:

~~~text
bounded security-like structural risk auditor
~~~

Boundary:

~~~text
Security status means structural risk inside supplied events. It is not legal, semantic, or operational final judgment.
~~~

Structural Observability foundation:

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- Foundation release: https://github.com/Tuttotorna/lon-mirror/releases/tag/v0.2.2
- DOI: https://doi.org/10.5281/zenodo.20379374

Role document:

- [Structural Observability Role](docs/STRUCTURAL_OBSERVABILITY_ROLE.md)
<!-- STRUCTURAL_OBSERVABILITY_ROLE_END -->
