"""
Integration tests for UNICC AI Safety Council SLM Platform.
Run with: pytest tests/
"""
import pytest


def get_client():
    from app.slm.api import app
    from fastapi.testclient import TestClient
    return TestClient(app)


def test_health():
    """Health endpoint should return 200 with model info."""
    client = get_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"


def test_evaluate_verimedia():
    """VeriMedia GitHub URL should be accepted and return structured output."""
    client = get_client()
    response = client.post(
        "/evaluate",
        json={"github_url": "https://github.com/FlashCarrot/VeriMedia"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "expert_outputs" in data
    assert "Governance Expert" in data["expert_outputs"]
    assert "Threat Expert" in data["expert_outputs"]
    assert "Behavioral Expert" in data["expert_outputs"]
    assert "final_council_recommendation" in data
    assert data["final_council_recommendation"]["final_decision"] in [
        "Approve", "Revise", "Escalate", "Reject"
    ]


def test_evaluate_invalid_url():
    """Non-GitHub URLs should return 422 validation error."""
    client = get_client()
    response = client.post(
        "/evaluate",
        json={"github_url": "https://notgithub.com/some/repo"}
    )
    assert response.status_code == 422


def test_github_url_to_request_verimedia():
    """VeriMedia URL should produce VeriMedia-specific RunRequest."""
    from app.slm.api import github_url_to_request
    req = github_url_to_request("https://github.com/FlashCarrot/VeriMedia")
    assert req.ai_system.name == "VeriMedia"
    assert len(req.evaluation_scenarios) >= 3
    assert "flask" in req.ai_system.purpose.lower() or "gpt" in req.ai_system.purpose.lower()


def test_report_endpoint():
    """Report endpoint should return markdown text."""
    client = get_client()
    response = client.post(
        "/report",
        json={"github_url": "https://github.com/FlashCarrot/VeriMedia"}
    )
    assert response.status_code == 200
    assert "UNICC AI Safety Council" in response.text
    assert "Final Council Decision" in response.text
