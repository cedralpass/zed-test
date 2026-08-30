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
    Wind: 20 knots, Weight: 180 lbs -> Expected: 12m (based on new engine logic)
    """
    payload = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    assert response.status_code == 200
    # Check if the result '12m' is in the response HTML
    assert b"12m" in response.data

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

def test_kite_calculation_inputs_persist(client):
    """Test that inputs persist after calculation (desired behavior)."""
    payload = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    # Check that the input fields ARE present in the response
    assert b'value="20"' in response.data
    assert b'value="180"' in response.data
    assert b'value="twintip"' in response.data

def test_invalid_input(client):
    """Test that invalid numeric input returns an error message."""
    payload = {
        'wind_speed': 'not_a_number',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    assert response.status_code == 200
    assert b"Please enter valid numeric values" in response.data

def test_kite_calculation_weight_adjustment(client):
    """Test that increasing weight increases the recommended kite size."""
    # Base case: 20 knots, 180 lbs, twintip -> 12m
    payload_base = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response_base = client.post('/', data=payload_base)
    assert b"12m" in response_base.data

    # 250 lbs is ~113.4kg. 113.4 - 75 = 38.4kg.
    # 38.4 * 0.05 = 1.92m. 11m + 1.92m = 12.92m -> 13m.
    payload_heavy = {
        'wind_speed': '20',
        'rider_weight': '250',
        'board_type': 'twintip'
    }
    response_heavy = client.post('/', data=payload_heavy)
    assert b"13m" in response_heavy.data

def test_kite_calculation_board_type_adjustment(client):
    """Test that surfboard and foil adjust the kite size."""
    # Base case: 20 knots, 180 lbs, twintip -> 12m
    payload_base = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response_base = client.post('/', data=payload_base)
    assert b"12m" in response_base.data

    # Surfboard: -2.0m -> 12m - 2.0m = 10m
    payload_surf = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'surfboard'
    }
    response_surf = client.post('/', data=payload_surf)
    assert b"10m" in response_surf.data

    # Foil: -2.0m -> 12m - 2.0m = 10m
    payload_foil = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'foil'
    }
    response_foil = client.post('/', data=payload_foil)
    assert b"10m" in response_foil.data
