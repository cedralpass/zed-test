# Ozone Reflex 2026 Sweetspot Wind Ranges (Knots)
# Based on the manufacturer graph provided.
# Format: { size_m: (min_knots, max_annots) }

OZONE_REF_2026_DATA = {
    13: (14, 18),
    12: (16, 20),
    11: (18, 22),
    10: (20, 24),
    9: (22, 26),
    8: (24, 28),
    7: (26, 30),
    6: (28, 32),
    5: (30, 34)
}

# Estimation Constants
ESTIMATION_BASELINE_WIND = 15  # knots
ESTIMATION_BASELINE_KITE = 15  # meters
ESTIMATION_WIND_ADJUST_RATE = -0.6  # m per knot
ESTIMATION_WEIGHT_BASELINE = 180  # lbs
ESTIMATION_WEIGHT_ADJUST_RATE = 1.0  # m per 10 lbs
