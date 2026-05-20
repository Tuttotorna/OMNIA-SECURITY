# Security Decision Boundary

## Purpose

This document prevents OMNIA-SECURITY from becoming a decision engine.

## Rule

OMNIA-SECURITY may adapt and observe.

OMNIA-SECURITY may report structural security-domain signals.

OMNIA-SECURITY may preserve evidence.

OMNIA-SECURITY must not declare final security decisions.

## Correct output

Correct:

structural drift observed
trust boundary shift measured
policy drift measured
validated envelope observed
measurement still required
saturation reached

Incorrect:

system is secure
system is unsafe
deploy is approved
deploy is blocked
artifact is compromised
actor is malicious

## Backbone path

All formal validation remains:

BoundaryCertificate
  -> omnia-limit
  -> OMNIA-VALIDATION

Any final governance decision remains external to the measurement backbone.
