from __future__ import annotations

from typing import Any

from omnia import build_boundary_certificate
from omnia_limit import validate_certificate
from omnia_validation.enveloper import process_boundary_step


def _coerce_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _coerce_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _clamp_01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _derive_security_deformation_index(measurement: dict[str, Any]) -> float:
    """Normalize security-domain signals into the backbone deformation field.

    OMNIA-SECURITY does not declare secure / insecure truth.

    It maps security-facing structural signals into the canonical measurement
    boundary used by the OMNIA backbone.
    """

    if "ast_deformation_index" in measurement:
        return _coerce_float(measurement["ast_deformation_index"])

    if "deformation_index" in measurement:
        return _coerce_float(measurement["deformation_index"])

    if "attack_surface_delta" in measurement:
        return _coerce_float(measurement["attack_surface_delta"])

    if "policy_drift" in measurement:
        return _coerce_float(measurement["policy_drift"])

    if "permission_drift" in measurement:
        return _coerce_float(measurement["permission_drift"])

    if "trust_boundary_shift" in measurement:
        return _coerce_float(measurement["trust_boundary_shift"])

    if "exposure_delta" in measurement:
        return _coerce_float(measurement["exposure_delta"])

    if "risk_signal" in measurement:
        return _coerce_float(measurement["risk_signal"])

    if "security_stability_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["security_stability_score"], 1.0))
        return 1.0 - score

    if "control_integrity_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["control_integrity_score"], 1.0))
        return 1.0 - score

    if "configuration_stability" in measurement:
        score = _clamp_01(_coerce_float(measurement["configuration_stability"], 1.0))
        return 1.0 - score

    return _coerce_float(
        measurement.get(
            "drift_score",
            measurement.get("delta_omega", measurement.get("delta", 0.0)),
        )
    )


def _derive_boundary_state(measurement: dict[str, Any], deformation_index: float) -> tuple[bool, bool, str]:
    """Derive explicit boundary fields without making final security decisions."""

    should_continue = measurement.get("should_continue")
    saturation_detected = measurement.get("saturation_detected")

    gate = str(
        measurement.get(
            "gate",
            measurement.get("gate_status", measurement.get("status", "")),
        )
    ).upper()

    if should_continue is None:
        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            should_continue = False
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            should_continue = True

    if saturation_detected is None:
        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            saturation_detected = True
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            saturation_detected = False

    if should_continue is None and saturation_detected is None:
        saturation_detected = deformation_index <= 0.05
        should_continue = not saturation_detected

    if should_continue is None:
        should_continue = not bool(saturation_detected)

    if saturation_detected is None:
        saturation_detected = not bool(should_continue)

    reason = measurement.get("reason")
    if reason is None:
        reason = (
            "Security-domain structural saturation reached"
            if bool(saturation_detected)
            else "Security-domain measurement still yields structural information"
        )

    return bool(should_continue), bool(saturation_detected), str(reason)


def _extract_security_extra_metrics(measurement: dict[str, Any]) -> dict[str, Any]:
    known_keys = {
        "ast_deformation_index",
        "deformation_index",
        "attack_surface_delta",
        "policy_drift",
        "permission_drift",
        "trust_boundary_shift",
        "exposure_delta",
        "risk_signal",
        "security_stability_score",
        "control_integrity_score",
        "configuration_stability",
        "drift_score",
        "delta_omega",
        "delta",
        "perturbation_step",
        "should_continue",
        "saturation_detected",
        "gate",
        "gate_status",
        "status",
        "reason",
    }

    return {
        key: value
        for key, value in measurement.items()
        if key not in known_keys and isinstance(value, (int, float, str, bool, type(None)))
    }


def adapt_security_measurement_to_boundary_certificate(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIA-SECURITY",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Adapt security-domain measurements into the canonical BoundaryCertificate.

    OMNIA-SECURITY is a Security Consumer / Domain Adapter.

    It does not define BoundaryCertificate.
    It does not define ValidationEnvelope.
    It does not validate schema directly.
    It does not declare secure / insecure final truth.
    """

    ast_deformation_index = _derive_security_deformation_index(measurement)
    perturbation_step = _coerce_int(measurement.get("perturbation_step", 0))
    should_continue, saturation_detected, reason = _derive_boundary_state(
        measurement,
        ast_deformation_index,
    )

    extra_metrics = _extract_security_extra_metrics(measurement)
    extra_metrics["domain"] = "security"

    for key in [
        "attack_surface_delta",
        "policy_drift",
        "permission_drift",
        "trust_boundary_shift",
        "exposure_delta",
        "risk_signal",
        "security_stability_score",
        "control_integrity_score",
        "configuration_stability",
    ]:
        if key in measurement:
            extra_metrics[key] = measurement[key]

    return build_boundary_certificate(
        target_repository=target_repository,
        ast_deformation_index=ast_deformation_index,
        perturbation_step=perturbation_step,
        should_continue=should_continue,
        saturation_detected=saturation_detected,
        reason=reason,
        certificate_id=certificate_id,
        timestamp=timestamp,
        extra_metrics=extra_metrics,
    )


def observe_security_envelope(envelope: dict[str, Any]) -> dict[str, Any]:
    """Observe a ValidationEnvelope from a security-domain viewpoint.

    This is observation, not decision.

    The returned object is a report over validated backbone output.
    It is not a competing ValidationEnvelope.
    """

    details = envelope.get("details", {})

    return {
        "observer": "OMNIA-SECURITY",
        "role": "security_consumer",
        "observed_status": envelope.get("validation_status"),
        "target_repository": details.get("target_repository"),
        "certificate_id": details.get("certificate_id"),
        "saturation_detected": details.get("saturation_detected"),
        "ast_deformation_index": details.get("ast_deformation_index"),
        "perturbation_step": details.get("perturbation_step"),
        "security_decision": None,
        "backbone_contract_preserved": True,
    }


def run_security_backbone_flow(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIA-SECURITY",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Run a security-domain measurement through the canonical OMNIA backbone.

    Flow:

    security-domain measurement
      -> OMNIA-SECURITY domain adapter
      -> BoundaryCertificate-compatible artifact
      -> omnia-limit validate_certificate()
      -> OMNIA-VALIDATION process_boundary_step()
      -> ValidationEnvelope
      -> OMNIA-SECURITY observation

    OMNIA-SECURITY only adapts and observes.
    """

    raw_certificate = adapt_security_measurement_to_boundary_certificate(
        measurement,
        target_repository=target_repository,
        certificate_id=certificate_id,
        timestamp=timestamp,
    )

    validate_certificate(raw_certificate)
    envelope = process_boundary_step(raw_certificate)

    return observe_security_envelope(envelope)
