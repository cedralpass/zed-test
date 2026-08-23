import math
from constants import OZONE_REF_2026_DATA, ESTIMATION_BASELINE_WIND, ESTIMATION_BASELINE_KITE, ESTIMATION_WIND_ADJUST_RATE, ESTIMATION_WEIGHT_BASELINE, ESTIMATION_WEIGHT_ADJUST_RATE
 
def get_kite_size(wind_speed_knots, rider_weight_lbs, board_type='twintip', use_library=True):
    """
    Calculates the recommended kite size.
    
    :param wind_speed_knots: Wind speed in knots.
    :param rider_weight_lbs: Rider weight in lbs.
    :param board_type: Type of board (twintip, surfboard, foil).
    :param use_library: If True, use the Ozone Reflex 2026 lookup. 
                        If False, use the estimation fallback.
    :return: Recommended kite size in meters (float/int).
    """
    base_size = 0.0
    
    if use_library:
        # Find the kite size whose sweetspot midpoint is closest to the current wind speed
        best_size = None
        min_distance = float('inf')
        
        for size, (min_wind, max_wind) in OZONE_REF_2026_DATA.items():
            midpoint = (min_wind + max_wind) / 2
            distance = abs(midpoint - wind_speed_knots)
            
            if distance < min_distance:
                min_distance = distance
                best_size = size
        
        if best_size is not None:
            base_size = float(best_size)
        else:
            # If no library match found (unlikely with this logic), fall back to estimation
            use_library = False
    
    if not use_library:
        # Estimation Logic
        # Base size at 15 knots is 15m.
        # Wind adjustment: -0.6m for every 1 knot increase/decrease.
        wind_diff = wind_speed_knots - ESTIMATION_BASELINE_WIND
        wind_adjustment = wind_diff * ESTIMATION_WIND_ADJUST_RATE
        base_size = ESTIMATION_BASELINE_KITE + wind_adjustment
 
    # Weight adjustment: +1m for every 20lbs above 180.
    weight_diff = rider_weight_lbs - ESTIMATION_WEIGHT_BASELINE
    weight_adjustment = (weight_diff / 20.0) * ESTIMATION_WEIGHT_ADJUST_RATE
    
    # Base twintip size including weight adjustment
    twintip_size = base_size + weight_adjustment
    
    # Board type adjustment
    if board_type == 'surfboard':
        recommended_size = twintip_size - 1.0
    elif board_type == 'foil':
        # For foil, divide twintip size by 2
        recommended_size = twintip_size / 2.0
    else:
        recommended_size = twintip_size
        
    return math.ceil(recommended_size)
