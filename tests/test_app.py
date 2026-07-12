from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_from_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200
    assert email in activities[activity_name]["participants"]

    unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
