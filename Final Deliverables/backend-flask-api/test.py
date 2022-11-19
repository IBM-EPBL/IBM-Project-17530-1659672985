import time
from locust import HttpUser, TaskSet, task, between

class SubClassTest(TaskSet):

    @task
    def main_page(self):
        self.client.headers = {'Authorization': 'Token 2603a281-4074-4fe9-b634-e1258e78e085'}
        self.client.get('/transaction')

    @task(2)
    def perihal_page(self):
        self.client.headers = {'Authorization': 'Token 2603a281-4074-4fe9-b634-e1258e78e085'}
        self.client.get('/budget')


class MainClassTest(HttpUser):
    tasks = [SubClassTest]
    wait_time = between(5, 10)