from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "test")

    response = client.get("/")
    body = response.json()

    assert response.status_code == 200
    assert body["service"] == "sre-demo"
    assert body["version"] == "test"
    assert body["pod"]


def test_healthz():
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz():
    response = client.get("/readyz")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
