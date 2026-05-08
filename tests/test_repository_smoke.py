
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "pytest.ini",
        "SECURITY_AT_A_GLANCE.md",
        "SECURITY_CASES.md",
        "docs/SECURITY_SCOPE.md",
        "docs/RESULTS_INDEX.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_current_experiment_files_exist():
    required = [
        "FIRST_SECURITY_EXPERIMENT.md",
        "FIRST_SECURITY_EXPERIMENT_RESULTS.md",
        "COLAB_FIRST_SECURITY_RUN_V0.md",
        "run_first_security_experiment.py",
        "SECOND_SECURITY_EXPERIMENT.md",
        "SECOND_SECURITY_EXPERIMENT_RESULTS.md",
        "COLAB_SECOND_SECURITY_RUN_V0.md",
        "run_second_security_experiment.py",
        "RUN_ALL_SECURITY_EXPERIMENTS.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required_phrases = [
        "measurement != inference != decision",
        "not a security scanner",
        "not a vulnerability scanner",
        "does not attack",
        "does not exploit",
        "Decision remains external",
    ]
    for phrase in required_phrases:
        assert phrase in text

def test_scope_boundary_terms():
    text = (ROOT / "docs" / "SECURITY_SCOPE.md").read_text(encoding="utf-8")
    required_phrases = [
        "diagnostic signal != confirmed vulnerability",
        "structural drift != exploit",
        "security-relevant measurement != security scanner",
        "decision remains external",
    ]
    for phrase in required_phrases:
        assert phrase in text

def test_citation_contains_doi():
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert "10.5281/zenodo.19879356" in text
