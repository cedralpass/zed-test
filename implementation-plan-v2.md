# Implementation Plan: Engine V2 (Advanced Coefficient Model)

## 🎯 Goal
Upgrade the kite selection logic from a simple baseline/lookup approach to a sophisticated **Coefficient-Based Adjustment** model. This model will better reflect the physical relationship between rider weight, wind energy, and equipment drag.

---

## 🧠 The Mathematical Model

The new engine will calculate the kite size based on a "Standard Rider/Board" baseline, applying additive or subtractive modifiers.

### The Formula
$$KiteSize = BaseSize(Wind) + \text{WeightAdjustment} + \text{BoardAdjustment}$$

### 1. $BaseSize(Wind)$
We will continue to use the **Ozone Reflex 2026** lookup table to find the "sweetspot" midpoint for the current wind speed. This ensures we are grounded in manufacturer-validated data.

### 2. $\text{WeightAdjustment}$
Adjusts for the mass of the rider relative to a standard baseline.
*   **Baseline Rider**: $75\text{kg}$ ($\approx 165\text{lbs}$)
*   **Adjustment Rate**: $+0.05\text{m}$ for every $1\text{kg}$ above $75\text{kg}$ (and $-0.05\text{m}$ below).

### 3. $\text{BoardAdjustment}$
Adjusts for the aerodynamic/hydrodynamic drag of the gear.
*   **Baseline Board**: `twintip` ($0\text{m}$ adjustment)
*   **`surfboard`**: $+1.5\text{m}$ (compensating for high drag/volume)
*   **`foil`**: $-2.0\text{m}$ (compensating for extremely low drag)

---

## 🚀 Execution Roadmap

### Phase A: Baseline Verification (The "Ground Truth")
**Objective**: Ensure we know exactly what the current engine produces so we can measure progress.

1.  Create `tests/test_engine_comparison.py`.
2.  Define a "Standard Test Suite" covering:
    *   **Scenario 1 (The User's Request)**: 80kg Rider, Twintip, Wind: [10, 15, 20, 25] knots.
    *   **Scenario 2 (Heavy Rider)**: 110kg Rider, Twintip, Wind: 15 knots.
    *   **Scenario 3 (High Drag)**: 80kg Rider, Surfboard, Wind: 15 knots.
    *   **Scenario 4 (Low Drag)**: 80kg Rider, Foil, Wind: 15 knots.
3.  Execute tests to capture `engine.py` outputs.

### Phase B: Implementation
**Objective**: Develop `enginev2.py`.

1.  Implement the mathematical model described above.
2.  Ensure the function signature remains compatible with the existing `app.py` (to allow for easy swapping).
3.  Use `math.ceil()` for the final result to provide a practical, actionable kite size.

### Phase C: The "Battle" (Validation)
**Objective**: Quantitatively prove the improvement.

1.  Run the comparison test suite against **both** `engine.py` and `enginev2.py`.
2.  Generate a Comparison Table in the test output:
    | Wind | Weight | Board | `engine.py` | `enginev2.py` | $\Delta$ |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | 15kt | 80kg | Twintip | 12m | 12m | 0 |
    | 15kt | 80kg | Foil | 6m | 10m | +4m |
3.  Analyze the $\Delta$ (Delta). A successful implementation will show significant, physically-grounded shifts in the `foil` and `surfboard` categories.

---

## 🛠 Tech Stack Requirements
*   **Language**: Python 3.13
*   **Testing**: `pytest`
*   **Dependencies**: `math`, `constants.py` (for Ozone data)
