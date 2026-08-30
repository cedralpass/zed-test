import math
from constants import OZONE_REF_2026_DATA

def get_kite_size(wind_speed_knots, rider_weight_lbs, board_type='twintip', use_library=True):
    """
    Advanced Kite Size Calculation (Engine V2)
    Uses a coefficient-based adjustment model.
    
    :param wind_speed_knots: Wind speed in knots.
    :param rider_weight_lbs: Rider weight in lbs.
    :param board_type: Type of board (twintip, surfboard, foil).
    :param use_library: Not used in V2 as we always use the manufacturer baseline.
    :return: Recommended kite size in meters (int).
    """
    # 1. Base Size from Wind (Manufacturer Baseline)
    base_size = 0.0
    best_size = None
    min_distance = float('1000')
    
    for size, (min_wind, max_wind) in OZONE_REF_2026_DATA.items():
        midpoint = (min_wind + max_wind) / 2
        distance = abs(midpoint - wind_speed_knots)
        
        if distance < min_distance:
            min_distance = distance
            best_size = size
            
    if best_size is not None:
        base_size = float(best_size)
    else:
        # Fallback if lookup fails
        base_size = 12.0

    # 2. Weight Adjustment
    # Standard rider is 75kg (~165.35 lbs). 
    # We add/subtract 0.05m for every 1kg deviation.
    weight_kg = rider_weight_lbs / 2.20462
    weight_diff_kg = weight_kg - 75.0
    weight_adjustment = weight_diff_kg * 0.05
    
    # 3. Board Type (Drag) Adjustment
    board_adjustments = {
        'twintip': 0.0,
        'surfboard': -2.0,
        'foil': -2.0
    }
    board_adjustment = board_adjustments.get(board_type, 0.0)
    
    # 4. Final Calculation
    recommended_size = base_size + weight_adjustment + board_adjustment
    
    print(f"DEBUG: wind={wind_speed_knots}, weight={rider_weight_lbs}, board={board_type}, base={base_size}, weight_adj={weight_adjustment}, board_adj={board_adjustment}, final={recommended_size}")

    return math.ceil(recommended_size)
