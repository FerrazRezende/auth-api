from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def login(self):

        login_data = {
            "username": "teste.stress",
            "password": "12345678"
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.client.post("/auth/login", data=login_data, headers=headers)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)