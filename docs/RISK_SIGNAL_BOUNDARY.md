# Risk Signal Boundary

This document defines the public boundary around OMNIA-SECURITY risk signals.

---

## Risk signal

A risk signal is a bounded diagnostic indication.

It means:

    external inspection may be justified

It does not mean:

    vulnerability confirmed
    exploit exists
    system is insecure
    decision is complete

---

## Structural anomaly

A structural anomaly is unexpected behavior under a declared diagnostic mode.

It may be relevant.

It may be benign.

It requires context.

---

## Instability

Instability means structural behavior changes, degrades, or fails to preserve a declared condition.

It may suggest fragility.

It does not automatically imply a security vulnerability.

---

## Boundary

These signals remain diagnostic-level signals.

They are not:

- exploit proof;
- vulnerability proof;
- security verdict;
- attack instruction;
- downstream decision.

The boundary remains:

    measurement != inference != decision

    Decision remains external

