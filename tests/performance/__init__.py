from locust import HttpUser, task


class User(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def portfolio(self):
        self.client.get("/art")

    @task
    def commissions(self):
        self.client.get("/commissions")
