import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_api():
    # Arrange
    client = APIClient()


    # Act
    response = client.get('/api/v1/products/')

    # Assert
    assert response.status_code == 200