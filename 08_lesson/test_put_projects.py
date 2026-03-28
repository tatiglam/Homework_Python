import pytest
import time


class TestUpdateProject:
    @pytest.mark.positive
    def test_update_project_title(self, api_client, test_project):
        new_title = f"Updated_{int(time.time())}"
        response = api_client.update_project(test_project, title=new_title)

        assert response.status_code == 200
        
        get_response = api_client.get_project(test_project)
        assert get_response.status_code == 200
        assert get_response.json()["title"] == new_title

    @pytest.mark.negative
    def test_update_project_not_found(self, api_client):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.update_project(fake_id, title="New Title")

        assert response.status_code == 404

    @pytest.mark.negative
    def test_update_project_empty_title(self, api_client, test_project):
        response = api_client.update_project(test_project, title="")
        assert response.status_code in [400, 422]

    @pytest.mark.negative
    def test_update_project_no_data(self, api_client, test_project):
        with pytest.raises(ValueError, match="No data to update"):
            api_client.update_project(test_project)
