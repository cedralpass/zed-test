# Wind Kite Picker App
Lets build a simple app using Python and the Flask framework for picking a Kite for Kite Surfing.

## Wind Speed
When kite surfing, the wind is the main driver of what kite you pick.  Low wind, a bigger kite. For example if the wind is 15knts, likely would be on a 15m kite.  As the wind picks up to 20knts it likely a 12m kite is the pick.  When its up to 25knts, a 10m or even an 8m is fun.  

Lots of kite manufactures have charts on when the kite is the best.

## Rider Weight
Rider weight also matters. I am around 196 lbs.  I usually have to have a bigger kite than someone who is 160 lbs.  So if someone lighter is on a 10m kite, I might go up to 12m.

## Board Type also matters

A twintip kiteboard is the normal.  With those smaller boards, you need a normal range of kites.  However, you can get a bigger twintip for a size down kite. Or even a kite surfboard, which would definately be one size down than normal.  

A foil boards. I do not know the ranges for those boards and kites, but the kites are much smaller. 


## Tech Stack & Architecture

### 1. Backend
- **Language**: Python 3.x
- **Framework**: Flask (Lightweight, minimal dependencies)
- **Logic**: All calculation engine and Ozone Reflex data will reside in a dedicated `constants.py` or `engine.py`.

### 2. Frontend
- **Structure**: HTML5
- **Styling**: Tailwind CSS (via CDN for zero-build complexity)
- **Interactivity**: Vanilla JavaScript (for instant, client-side updates without page reloads)

### 3. Design Principles
- **Mobile-First**: Optimized for one-handed use on a smartphone at the beach.
- **High Contrast/High Visibility**: Large touch targets and clear typography for use in bright, sunny environments.
- **Zero-Dependency UI**: Avoid heavy JS frameworks (React/Vue) to keep the "Time to Interactive" near-instant.
- **Wind Speed**: Support for Knots (primary) and MPH.
- **Rider Weight**: Support for Lbs and Kilograms.
- **Board Type**: Selection between Twintip, Surfboard, and Foil.

### 2. Calculation Logic
#### V1: Opinionated "Sweetspot" Mode (Primary)
- **Logic**: The app will attempt to match the current wind speed to the **Sweetspot** range of a kite.
- **Default Data**: For V1, the "Sweetspot" wind ranges for kite sizes (5m–13m) will be hardcoded using the **Ozone Reflex 2026** manufacturer graph.
- **User Override**: The user can manually select a larger kite (e.g., moving from the Sweetspot to the "Intermediate" range) if they choose.

#### Fallback: Estimation Mode (Secondary)
- **Use Case**: When no specific kite is selected from the library.
- **Baseline**: 15 knots $\approx$ 15m kite.
- **Wind Adjustment**: For every 1 knot increase in wind speed, decrease kite size by 0.6m.
- **Weight Adjustment**: 
    - Baseline weight: 180 lbs.
    - For every +10 lbs above 180, increase kite size by 1m.
    - For every -10 lbs below 180, decrease kite size by 1m.

### 3. Data Management & Profiles
- **User Profile**: Store user-specific weight, preferred board types, and kite brands/models.
- **Gear Library**: 
    - **Kites**: Store brand/model specific wind ranges.
    - **Boards**: Store board volumes (to account for drag/floatation).

### 4. Safety & Constraints
- **Wind Limit**: Default warning/cutoff at 35 knots.
- **Extreme Mode**: Ability to bypass the 35-knot limit for experienced/extreme users.
