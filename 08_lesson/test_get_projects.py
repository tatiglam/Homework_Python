import pytest


class TestGetProject:
    @pytest.mark.positive
    def test_get_project_success(self, api_client, test_project):
        response = api_client.get_project(test_project)

        assert response.status_code == 200
        assert response.json()["id"] == test_project
        assert "title" in response.json()

    @pytest.mark.negative
    def test_get_project_not_found(self, api_client):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.get_project(fake_id)

        assert response.status_code == 404

    @pytest.mark.negative
    def test_get_project_invalid_id(self, api_client):
        response = api_client.get_project("123")
        assert response.status_code in [400, 404]
