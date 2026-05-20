# OMNIA-SECURITY

## DOI

[![DOI](https://zenodo.org/badge/1224259075.svg)](https://zenodo.org/badge/latestdoi/1224259075)

Release DOI:

    10.5281/zenodo.19879356

Zenodo latest DOI link:

    https://doi.org/10.5281/zenodo.19879356

GitHub release:

    https://github.com/Tuttotorna/OMNIA-SECURITY/releases/tag/v1.0.0

**Bounded structural diagnostics for security-relevant traces.**

OMNIA-SECURITY is the security-relevant diagnostic layer of the MB-X.01 / OMNIA ecosystem.

DOI:

    10.5281/zenodo.19879356

Its role is narrow:

    security-relevant trace -> structural diagnostic -> risk signal -> external security decision

It asks one question:

    does this security-relevant trace show structural behavior worth external inspection?

OMNIA-SECURITY is not the ecosystem landing page.

It is not the validation showroom.

It is not the OMNIA core measurement engine.

It is not a security scanner.

It is not a vulnerability scanner.

It is not an exploit tool.

It is not a vulnerability verdict engine.

It does not attack.

It does not exploit.

It performs bounded structural diagnostics only.

Canonical boundary:

    measurement != inference != decision

    Decision remains external

---

## Start here

From a clean environment:

    git clone https://github.com/Tuttotorna/OMNIA-SECURITY.git
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

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical ecosystem entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Transformation and invariance layer |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Stable-region falsification layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |

---

## Ecosystem entry point

For the full ecosystem map, start here:

    https://github.com/Tuttotorna/lon-mirror

For public validation artifacts, start here:

    https://github.com/Tuttotorna/OMNIA-VALIDATION

For core structural measurement, start here:

    https://github.com/Tuttotorna/OMNIA

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

## License

MIT.

