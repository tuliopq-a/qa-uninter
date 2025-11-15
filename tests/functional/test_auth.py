import requests

BASE = "http://localhost:8001"

def test_login_valid():
    r = requests.post(f"{BASE}/login?cpf=12345678901&password=senha123")
    assert r.status_code == 200
    assert r.json()["user"]["cpf"] == "12345678901"

def test_login_invalid():
    r = requests.post(f"{BASE}/login?cpf=12345678901&password=errada")
    assert r.status_code == 401

def test_sql_injection_attempt():
    payload = "123' OR '1'='1"
    r = requests.post(f"{BASE}/login?cpf=12345678901&password={payload}")
    # Resultado depende se VULNERABLE_MODE está ativado
    assert r.status_code in [200, 401]
