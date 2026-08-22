import unittest
from engine import get_kite_size

class TestKiteEngine(unittest.TestCase):
    
    def test_ozone_reflex_lookup_success(self):
        """
        Integration Test: 80kg user (~176lbs), twintip, 20 knots
        should pick an 11m Ozone reflex 2026 kite because its 
        sweetspot (18-22) is closest to 20 knots.
        """
        weight_lbs = 176.37
        wind_knots = 20
        board = 'twintip'
        
        result = get_kite_size(wind_knots, weight_lbs, board, use_library=True)
        self.assertEqual(result, 11, f"Expected 11m kite, but got {result}m")

    def test_estimation_fallback(self):
        """
        Test the estimation logic independently.
        15 knots, 180 lbs should result in 15m.
        """
        result = get_kite_size(15, 180, 'twintip', use_library=False)
        self.assertEqual(result, 15)

    def test_estimation_wind_increase(self):
        """
        Test estimation: 20 knots, 180 lbs should result in 12m (15 - 3).
        """
        result = get_kite_size(20, 180, 'twintip', use_library=False)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
