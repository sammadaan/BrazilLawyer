def test_health_check(client):
    resp = client.get("/admin/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_case_listing(client):
    resp = client.get("/cases/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)