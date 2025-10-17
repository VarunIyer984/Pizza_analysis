import pytest
from main import app # Imports the Flask app from your app.py

@pytest.fixture
def client():
    """Creates a test client for our app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_imports_correctly():
    """Test 1: Check that the app object exists."""
    assert app is not None
    assert app.__class__.__name__ == 'Flask'
    print("Test 1 Passed: App imported successfully.")

def test_predict_route_handles_missing_model(client):
    """
    Test 2: Check the /predict route.
    The CI runner does NOT have the .pkl file, so your app.py
    will correctly set 'model = None'. This test confirms
    that your API returns the correct error in that situation.
    This is a very good test of your app's error handling.
    """
    test_data = {
        "pizza_category": "Classic",
        "pizza_size": "L",
        "unit_price": 20.0
    }

    # Send a POST request to the test client
    response = client.post('/predict', json=test_data)

    # Check that the server responded with an error (500)
    assert response.status_code == 500

    # Check that it sent the correct JSON error message
    assert response.json['error'] == 'Model not loaded.'

    print("Test 2 Passed: API correctly handles a missing model.")