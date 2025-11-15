from locust import HttpUser, task, between
import random

class AppointmentLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def list_appointments(self):
        self.client.get("/appointments")

    @task
    def create_appointment(self):
        patient_id = random.choice([1, 2])
        self.client.post("/appointments", params={
            "patient_id": patient_id,
            "doctor_name": "Dr Load Test",
            "appointment_date": "2025-05-01 10:00"
        })
