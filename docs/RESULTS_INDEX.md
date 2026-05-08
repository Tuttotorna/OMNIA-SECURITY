# OMNIA-SECURITY Results Index

## Purpose

This file gives a public entrypoint into current OMNIA-SECURITY experiments and result notes.

## Experiment 01 — Configuration drift vs surface stability

Files:

- `FIRST_SECURITY_EXPERIMENT.md`
- `FIRST_SECURITY_EXPERIMENT_RESULTS.md`
- `COLAB_FIRST_SECURITY_RUN_V0.md`
- `run_first_security_experiment.py`

Core distinction:

```text
surface similarity != structural equivalence
```

Purpose:

- show how a configuration may remain superficially operational while security-relevant structure changes
- measure drift rather than declare vulnerability

## Experiment 02 — Log instability before visible failure

Files:

- `SECOND_SECURITY_EXPERIMENT.md`
- `SECOND_SECURITY_EXPERIMENT_RESULTS.md`
- `COLAB_SECOND_SECURITY_RUN_V0.md`
- `run_second_security_experiment.py`

Core distinction:

```text
log availability != log structural stability
```

Purpose:

- show how log trajectories may remain parseable while structural instability emerges
- measure drift before treating the case as an operational security conclusion

## External run note

File:

- `SECURITY_EXTERNAL_RUN.md`

Purpose:

- records external / broader run context

## Runner

File:

- `RUN_ALL_SECURITY_EXPERIMENTS.py`

Purpose:

- runs current bounded structural security experiments

## Reading rule

```text
experiment result = bounded structural diagnostic output
bounded structural diagnostic output != production security decision
bounded structural diagnostic output != confirmed exploit
```
