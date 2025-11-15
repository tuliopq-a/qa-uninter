import requests

BASE = "http://localhost:8002"

def test_list_patients():
    r = requests.get(f"{BASE}/patients")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_create_patient():
    r = requests.post(
        f"{BASE}/patients?name=Teste&cpf=99988877766&birth_date=1990-01-01"
    )
    assert r.status_code in [200, 400]
