import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    # Arrange
    original_activities = copy.deepcopy(app_module.activities)

    # Act
    with TestClient(app_module.app) as test_client:
        yield test_client

    # Teardown
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
