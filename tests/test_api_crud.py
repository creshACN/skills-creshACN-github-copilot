import pytest

def test_get_activities(client, sample_activities):
    """Test retrieving all activities."""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == len(sample_activities)
    # Check that a known activity is present
    assert "Chess Club" in data
    assert data["Chess Club"]["description"] == sample_activities["Chess Club"]["description"]

def test_signup_for_activity(client):
    """Test signing up for an activity."""
    response = client.post("/activities/Chess Club/signup?email=test@example.com")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "test@example.com" in data["message"]
    assert "Chess Club" in data["message"]

    # Verify the participant was added
    response = client.get("/activities")
    activities = response.json()
    assert "test@example.com" in activities["Chess Club"]["participants"]

def test_unregister_from_activity(client):
    """Test unregistering from an activity."""
    # First, sign up
    client.post("/activities/Programming Class/signup?email=test@example.com")

    # Then unregister
    response = client.post("/activities/Programming Class/unregister?email=test@example.com")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "test@example.com" in data["message"]
    assert "Programming Class" in data["message"]

    # Verify the participant was removed
    response = client.get("/activities")
    activities = response.json()
    assert "test@example.com" not in activities["Programming Class"]["participants"]