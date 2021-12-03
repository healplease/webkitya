import os
import time
from base64 import b64encode

import locust.stats
from dotenv import load_dotenv, find_dotenv
from locust import HttpUser, task, between

locust.stats.CSV_STATS_INTERVAL_SEC = 5
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 15
load_dotenv(find_dotenv())

# commands: 
# UI mode:  locust -f tests/performance/__init__.py
# headless: locust -f tests/performance/__init__.py --headless -u 100 -r 2 -t 60s --html results.html

def auth_headers():
    username = os.environ.get("FLASK_ADMIN_USERNAME")
    password = os.environ.get("FLASK_ADMIN_PASSWORD")  # for local usage only
    auth = b64encode(f"{username}:{password}".encode()).decode()
    return {"Authorization": f"Basic {auth}"}


class User(HttpUser):
    abstract = True
    wait_time = between(3, 15)
    host = os.environ.get("SERVER_NAME", "http://0.0.0.0:8000")


class WalkthroughUser(User):
    weight = 15

    @task
    def walkthrough(self):
        self.client.get("/")
        self.client.get("/art")
        self.client.get("/commissions")
        self.client.post("/commissions")


class RandomLinkUser(User):
    weight = 3

    @task
    def index(self):
        self.client.get("/")

    @task
    def portfolio(self):
        self.client.get("/art")

    @task
    def commissions(self):
        self.client.get("/commissions")


class Admin(User):
    weight = 1

    @task
    def index(self):
        self.client.get("/admin", headers=auth_headers())

    @task
    def pages(self):
        self.client.get("/admin", headers=auth_headers())
        self.client.get("/admin/mainpage", headers=auth_headers())
        self.client.get("/admin/portfoliopage", headers=auth_headers())
        self.client.get("/admin/commissionspage", headers=auth_headers())
