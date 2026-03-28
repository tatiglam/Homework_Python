import pytest
import time


class TestCreateProject:
    @pytest.mark.positive
    def test_create_project_success(self, api_client):
        title = f"Test_{int(time.time())}"
        response = api_client.create_project(title)

        assert response.status_code == 201
        assert "id" in response.json()

        project_id = response.json()["id"]

        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()["title"] == title

    @pytest.mark.negative
    def test_create_project_empty_title(self, api_client):
        with pytest.raises(ValueError, match="Title cannot be empty"):
            api_client.create_project("")

    @pytest.mark.negative
    def test_create_project_whitespace_title(self, api_client):
        with pytest.raises(ValueError, match="Title cannot be empty"):
            api_client.create_project("   ")
