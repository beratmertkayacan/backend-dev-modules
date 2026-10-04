import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture(autouse=True)
def temiz_depo():
    """Her testten önce ve sonra bellek içi depoyu sıfırla."""
    main.tasks.clear()
    yield
    main.tasks.clear()


client = TestClient(main.app)


def test_liste_baslangicta_bos():
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.json() == []


def test_gorev_olusturma():
    r = client.post("/tasks", json={"title": "Backend çalış", "priority": "high"})
    assert r.status_code == 201
    assert r.json() == {"title": "Backend çalış", "priority": "high", "id": 1, "done": False}


def test_varsayilan_oncelik_medium():
    r = client.post("/tasks", json={"title": "Varsayılan"})
    assert r.json()["priority"] == "medium"


def test_gecersiz_oncelik_reddedilir():
    r = client.post("/tasks", json={"title": "X", "priority": "acil"})
    assert r.status_code == 422


def test_tek_gorev_getirme():
    client.post("/tasks", json={"title": "A"})
    assert client.get("/tasks/1").json()["title"] == "A"


def test_olmayan_gorev_404():
    assert client.get("/tasks/99").status_code == 404


def test_ikinci_gorevi_tamamlama():
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    r = client.patch("/tasks/2")
    assert r.status_code == 200
    assert r.json()["done"] is True
    assert client.get("/tasks/1").json()["done"] is False


def test_olmayan_gorevi_tamamlama_404():
    assert client.patch("/tasks/5").status_code == 404


def test_ikinci_gorevi_silme():
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    assert client.delete("/tasks/2").status_code == 204
    assert [t["id"] for t in client.get("/tasks").json()] == [1]


def test_olmayan_gorevi_silme_404():
    assert client.delete("/tasks/7").status_code == 404


def test_yeni_id_en_buyuk_idnin_bir_fazlasi():
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    client.delete("/tasks/1")
    r = client.post("/tasks", json={"title": "C"})
    assert r.json()["id"] == 3
