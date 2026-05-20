# OMNIA-SECURITY Backbone Compliance

## Role

OMNIA-SECURITY is a Security Consumer / Domain Adapter.

It adapts security-domain structural measurements into the canonical OMNIA backbone.

It observes validated backbone output.

It is not the measurement core.

It is not the boundary validator.

It is not the validation control plane.

It is not a decision engine.

## Canonical flow

OMNIA-SECURITY must use the existing backbone:

security-domain measurement
  -> OMNIA-SECURITY domain adapter
  -> BoundaryCertificate-compatible artifact
  -> omnia-limit validate_certificate()
  -> OMNIA-VALIDATION process_boundary_step()
  -> ValidationEnvelope
  -> OMNIA-SECURITY observation

## Public API

OMNIA-SECURITY exposes:

adapt_security_measurement_to_boundary_certificate(...)
run_security_backbone_flow(...)
observe_security_envelope(...)

## Contract rule

OMNIA-SECURITY does not redefine BoundaryCertificate.

OMNIA-SECURITY does not redefine ValidationEnvelope.

OMNIA-SECURITY does not bypass omnia-limit.

OMNIA-SECURITY does not bypass OMNIA-VALIDATION.

OMNIA-SECURITY does not declare final secure / insecure truth.

## Security-domain mapping

attack_surface_delta
  -> ast_deformation_index

policy_drift
  -> ast_deformation_index

permission_drift
  -> ast_deformation_index

trust_boundary_shift
  -> ast_deformation_index

exposure_delta
  -> ast_deformation_index

risk_signal
  -> ast_deformation_index

security_stability_score
  -> ast_deformation_index = 1.0 - security_stability_score

control_integrity_score
  -> ast_deformation_index = 1.0 - control_integrity_score

configuration_stability
  -> ast_deformation_index = 1.0 - configuration_stability

## Forbidden interpretation

OMNIA-SECURITY must not emit final labels such as:

secure
unsafe
safe
compromised
approved
blocked

Those are downstream governance decisions.

OMNIA-SECURITY may report validated structural evidence.

## Boundary

security evidence != security decision
domain adapter != validator
validator != control plane
control plane != governance
governance != measurement

OMNIA-SECURITY stays in the Security Consumer / Domain Adapter layer.
