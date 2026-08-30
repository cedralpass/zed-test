from app import app

def test_debug_surfboard():
    with app.test_client() as client:
        payload = {
            'wind_speed': '20',
            'rider_weight': '180',
            'board_type': 'surfboard'
        }
        response = client.post('/', data=payload)
        print(f"Status: {response.status_code}")
        print(f"Data: {response.data}")
        # In enginev2, 20kn, 180lb, surfboard should be 14m
        assert b"14m" in response.data

if __name__ == "__main__":
    test_debug_surfboard()
