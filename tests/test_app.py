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
        'rider_weight': '18  ',
        'board_type': 'twintip'
    }
    response = client.post('/', data=payload)
    
    assert response.status_code == 200
    assert b"Please enter valid numeric values" in response.data

def test_kite_calculation_weight_adjustment(client):
    """Test that increasing weight increases the recommended kite size."""
    # Base case: 20 knots, 180 lbs, twintip -> 11m
    payload_base = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response_base = client.post('/', data=payload_base)
    assert b"11m" in response_base.data

    # 250 lbs is +70 lbs from 180. 
    # According to new requirement: +1m for every 20lbs.
    # So 70/20 = 3.5m increase. 11m + 3.5m = 14.5m, which rounds to 15m.
    payload_heavy = {
        'wind_speed': '20',
        'rider_weight': '250',
        'board_type': 'twintip'
    }
    response_heavy = client.post('/', data=payload_heavy)
    assert b"15m" in response_heavy.data

def test_kite_calculation_board_type_adjustment(client):
    """Test that surfboard and foil adjust the kite size."""
    # Base case: 20 knots, 180 lbs, twintip -> 11m
    payload_base = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'twintip'
    }
    response_base = client.post('/', data=payload_base)
    assert b"11m" in response_base.data

    # Surfboard: "one size down than normal" -> 11m - 1m = 10m
    payload_surf = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'surfboard'
    }
    response_surf = client.post('/', data=payload_surf)
    assert b"10m" in response_surf.data

    # Foil: divide twintip size by 2 and round up -> 11m / 2 = 5.5m -> 6m
    payload_foil = {
        'wind_speed': '20',
        'rider_weight': '180',
        'board_type': 'foil'
    }
    response_foil = client.post('/', data=payload_foil)
    assert b"6m" in response_foil.data
