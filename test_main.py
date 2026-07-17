from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_create_task():
    res = client.post("/tasks", json={"title": "Fix the bug"})
    assert res.status_code == 201
    assert res.json()["title"] == "Fix the bug"

def test_get_tasks():
    res = client.get("/tasks")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_delete_task():
    create = client.post("/tasks", json={"title": "Delete me"})
    task_id = create.json()["id"]
    res = client.delete(f"/tasks/{task_id}")
    assert res.status_code == 200

def test_delete_nonexistent():
    res = client.delete("/tasks/99999")
    assert res.status_code == 404