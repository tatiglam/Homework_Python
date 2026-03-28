import requests
from config import Config


class YougileAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.session = requests.Session()
        self.session.headers.update(Config.get_headers())

    def create_project(self, title, users=None):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        payload = {"title": title.strip()}
        if users:
            payload["users"] = users

        response = self.session.post(
            f"{self.base_url}/projects", json=payload
        )
        return response

    def get_project(self, project_id):
        if not project_id:
            raise ValueError("Project ID cannot be empty")
        return self.session.get(
            f"{self.base_url}/projects/{project_id}"
        )

    def update_project(self, project_id, title=None, users=None):
        if not project_id:
            raise ValueError("Project ID cannot be empty")

        payload = {}
        if title is not None:
            payload["title"] = title.strip()
        if users is not None:
            payload["users"] = users

        if not payload:
            raise ValueError("No data to update")

        url = f"{self.base_url}/projects/{project_id}"
        return self.session.put(url, json=payload)

    def close(self):
        self.session.close()
