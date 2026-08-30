import pytest
import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

try:
    from engine import get_kite_size as engine_v1
except ImportError:
    engine_v1 = None

try:
    from enginev2 import get_kite_size as engine_v2
except ImportError:
    engine_v2 = None

# Test Scenarios
SCENARIOS = [
    {"wind": 10, "weight": 176, "board": "twintip", "label": "80kg/Twintip/10kt"},
    {"wind": 15, "weight": 176, "board": "twintip", "label": "80kg/Twintip/15kt"},
    {"wind": 20, "weight": 176, "board": "twintip", "label": "80kg/Twintip/20kt"},
    {"wind": 25, "weight": 176, "board": "twintip", "label": "80kg/Twintip/25kt"},
    {"wind": 15, "weight": 242, "board": "twintip", "label": "110kg/Twintip/15kt"},
    {"wind": 15, "weight": 176, "board": "surfboard", "label": "80kg/Surfboard/15kt"},
    {"wind": 15, "weight": 176, "board": "foil", "label": "80kg/Foil/15kt"},
]

def test_engine_comparison():
    if engine_v1 is None or engine_v2 is None:
        pytest.fail("One of the engines could not be imported. Check your paths.")

    print("\n" + "="*80)
    print(f"{'SCENARIO':<30} | {'V1 (Old)':<10} | {'V2 (New)':<10} | {'DELTA':<10}")
    print("-" * 80)

    all_passed = True
    for s in SCENARIOS:
        v1_res = engine_v1(s["wind"], s["weight"], s["board"], use_library=True)
        v2_res = engine_v2(s["wind"], s["weight"], s["board"])
        
        delta = v2_res - v1_res
        
        print(f"{s['label']:<30} | {v1_res:>7}m | {v2_res:>7}m | {delta:>+7}m")
        
        # We don't fail the test if they are different! 
        # We are intentionally measuring the difference.
    
    print("="*80)
    print("Comparison Complete.")

if __name__ == "__main__":
    # This allows running the script directly to see the table
    pytest.main([__file__, "-s"])
