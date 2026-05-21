# OMNIA-SECURITY

<!-- ZENODO DOI:START -->

## DOI

[![DOI](https://zenodo.org/badge/1224259075.svg)](https://zenodo.org/badge/latestdoi/1224259075)

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIA-SECURITY
GitHub repository id: 1224259075
Latest release DOI: pending Zenodo publication or resolved dynamically by Zenodo badge

<!-- ZENODO DOI:END -->


## DOI

[![DOI](https://zenodo.org/badge/1224259075.svg)](https://zenodo.org/badge/latestdoi/1224259075)

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
