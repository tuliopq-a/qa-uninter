from locust import HttpUser, task, between

class AuthLoadTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def login(self):
        self.client.post("/login", params={
            "cpf": "12345678901",
            "password": "senha123"
        })
