import requests

BASE = "http://localhost:8003"

def test_list_appointments():
    r = requests.get(f"{BASE}/appointments")
    assert r.status_code == 200

def test_create_appointment():
    r = requests.post(
        f"{BASE}/appointments?patient_id=1&doctor_name=Dr.%20QA&appointment_date=2025-05-01%2010:00"
    )
    assert r.status_code in [200, 404]
