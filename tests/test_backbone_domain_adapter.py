from omnia_security import (
    adapt_security_measurement_to_boundary_certificate,
    observe_security_envelope,
    run_security_backbone_flow,
)
from omnia_limit import validate_certificate


def test_adapt_security_measurement_to_boundary_certificate_continue_flow():
    measurement = {
        "attack_surface_delta": 0.22,
        "perturbation_step": 2,
        "gate_status": "CONTINUE",
        "security_context": "api_boundary",
        "control_family": "access_policy",
    }

    raw_certificate = adapt_security_measurement_to_boundary_certificate(
        measurement,
        target_repository="OMNIA-SECURITY",
        certificate_id="security-boundary-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    cert = validate_certificate(raw_certificate)

    assert cert.certificate_id == "security-boundary-cert"
    assert cert.target_repository == "OMNIA-SECURITY"
    assert cert.ast_deformation_index == 0.22
    assert cert.perturbation_step == 2
    assert cert.should_continue is True
    assert cert.saturation_detected is False
    assert raw_certificate["metrics"]["domain"] == "security"
    assert raw_certificate["metrics"]["security_context"] == "api_boundary"
    assert raw_certificate["metrics"]["control_family"] == "access_policy"
    assert raw_certificate["metrics"]["attack_surface_delta"] == 0.22


def test_run_security_backbone_flow_stop_flow():
    measurement = {
        "security_stability_score": 0.97,
        "perturbation_step": 5,
        "gate_status": "STOP",
        "security_context": "supply_chain",
        "control_family": "artifact_integrity",
    }

    observation = run_security_backbone_flow(
        measurement,
        target_repository="OMNIA-SECURITY",
        certificate_id="security-stop-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-SECURITY"
    assert observation["role"] == "security_consumer"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "security-stop-cert"
    assert observation["target_repository"] == "OMNIA-SECURITY"
    assert observation["saturation_detected"] is True
    assert round(observation["ast_deformation_index"], 2) == 0.03
    assert observation["perturbation_step"] == 5
    assert observation["security_decision"] is None
    assert observation["backbone_contract_preserved"] is True


def test_run_security_backbone_flow_continue_flow():
    measurement = {
        "permission_drift": 0.18,
        "perturbation_step": 1,
        "gate_status": "CONTINUE",
        "security_context": "identity_boundary",
        "control_family": "least_privilege",
    }

    observation = run_security_backbone_flow(
        measurement,
        target_repository="OMNIA-SECURITY",
        certificate_id="security-continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-SECURITY"
    assert observation["role"] == "security_consumer"
    assert observation["observed_status"] == "GATE_OPEN_MEASUREMENT_REQUIRED"
    assert observation["certificate_id"] == "security-continue-cert"
    assert observation["target_repository"] == "OMNIA-SECURITY"
    assert observation["saturation_detected"] is False
    assert observation["ast_deformation_index"] == 0.18
    assert observation["perturbation_step"] == 1
    assert observation["security_decision"] is None
    assert observation["backbone_contract_preserved"] is True


def test_observe_existing_envelope_without_security_decision():
    envelope = {
        "envelope_id": "security-env",
        "timestamp": "2026-05-20T20:00:00Z",
        "validation_status": "GATE_CLOSED_SATURATION_REACHED",
        "details": {
            "target_repository": "OMNIA",
            "certificate_id": "existing-security-cert",
            "saturation_detected": True,
            "ast_deformation_index": 0.04,
            "perturbation_step": 9,
        },
    }

    observation = observe_security_envelope(envelope)

    assert observation["observer"] == "OMNIA-SECURITY"
    assert observation["role"] == "security_consumer"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "existing-security-cert"
    assert observation["target_repository"] == "OMNIA"
    assert observation["security_decision"] is None
    assert observation["backbone_contract_preserved"] is True
