from locust import HttpUser, task, between
import random

class PatientLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def list_patients(self):
        self.client.get("/patients")

    @task
    def create_patient(self):
        cpf = str(random.randint(10000000000, 99999999999))
        self.client.post("/patients", params={
            "name": "Teste Locust",
            "cpf": cpf,
            "birth_date": "1990-01-01"
        })
