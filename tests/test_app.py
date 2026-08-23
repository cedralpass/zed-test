import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Wind Kite Picker" in response.data

def test_kite_calculation_success(client):
    """
    Test the end-to-end calculation flow.
    Wind: 20 knots, Weight: 180 lbs -> Expected: 11m (based on engine logic)
    """
    payload = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    assert response.status_code == 200
    # Check if the result '11m' is in the response HTML
    assert b"11m" in response.data

def test_kite_calculation_extreme_wind(client):
    """Test that extreme wind triggers the warning message."""
    payload = {
        'wind_speed': '40',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    assert response.status_code == 200
    assert b"Warning: Extreme wind speed! Be careful." in response.data

def test_invalid_input(client):
    """Test that invalid numeric input returns an error message."""
    payload = {
        'wind_speed': 'not_a_number',
        'rider_weight': '18  ',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    assert response.status_code == 200
    assert b"Please enter valid numeric values" in response.data
