import pytest

def test_signup_nonexistent_activity(client):
    """Test signing up for a non-existent activity returns 404."""
    response = client.post("/activities/Nonexistent Activity/signup?email=test@example.com")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]

def test_signup_already_signed_up(client):
    """Test signing up for an activity when already signed up returns 400."""
    # Sign up first
    client.post("/activities/Gym Class/signup?email=test@example.com")

    # Try to sign up again
    response = client.post("/activities/Gym Class/signup?email=test@example.com")
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student already signed up for this activity" in data["detail"]

def test_unregister_nonexistent_activity(client):
    """Test unregistering from a non-existent activity returns 404."""
    response = client.post("/activities/Nonexistent Activity/unregister?email=test@example.com")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]

def test_unregister_not_signed_up(client):
    """Test unregistering from an activity when not signed up returns 400."""
    response = client.post("/activities/Basketball Team/unregister?email=test@example.com")
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student is not signed up for this activity" in data["detail"]