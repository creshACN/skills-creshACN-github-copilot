import pytest
from fastapi.testclient import TestClient
from src.app import app, activities as original_activities

@pytest.fixture
def client():
    """Provides a FastAPI TestClient instance for testing."""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Resets the activities dictionary to its original state before each test."""
    from src.app import activities
    activities.clear()
    activities.update(original_activities.copy())

@pytest.fixture
def sample_activities():
    """Provides a copy of the original activities data for test reference."""
    return original_activities.copy()