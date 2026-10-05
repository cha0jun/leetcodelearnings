import pytest
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

@pytest.fixture(autouse=True)
def reset_db():
    main.DB.clear()
    
def make(title="Broken light", category="lighting"):
    return client.post("/requests", json={"title": title, "category": category})

def test_create_defaults_to_open():
    r = make()
    assert r.status_code == 201
    assert r.json()["status"] == 'open'
    
def test_empty_title_rejected():
    assert make(title="").status_code == 422

def test_get_missing_404():
    assert client.get("/requests/999").status_code == 404


def test_filter_and_pagination():
    for i in range(3):
        make(title=f"t{i}")
    make(category="drains")
    assert len(client.get("/requests?category=drains").json()) == 1
    assert len(client.get("/requests?limit=2").json()) == 2


def test_illegal_transition_409():
    rid = make().json()["id"]
    r = client.patch(f"/requests/{rid}/status", json={"status": "resolved"})
    assert r.status_code == 409


def test_legal_transition():
    rid = make().json()["id"]
    r = client.patch(f"/requests/{rid}/status", json={"status": "in_progress"})
    assert r.json()["status"] == "in_progress"