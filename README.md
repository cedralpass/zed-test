# 🪁 Wind Kite Picker App

A lightweight, mobile-first web application designed to help kite surfers select the optimal kite size based on real-time wind speed, rider weight, and board type.

## 🎯 Project Overview

Choosing the right kite is critical for a safe and fun session. This app provides two way of determining your kite size:

1.  **Ozone Reflex 2026 "Sweetspot" Lookup**: Using authoritative manufacturer data, the app identifies the kite size whose optimal wind range (Sweetspot) is closest to the current wind speed. This helps account for the fluctuations (gusts and lulls) common in kite surfing.
2.  **Estimation Fallback**: If no specific kite is selected, the app uses a mathematical estimation model (based on a 15kt/15m baseline) to provide a quick recommendation.

## 🛠 Tech Stack

- **Core Logic**: Python 3.x
- **Web Framework**: Flask (Planned)
- **Styling**: Tailwind CSS via CDN (Planned)
- **Testing**: `unittest` (Python)

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Running Tests
The core calculation engine is already verified with automated tests. To run them:

```bash
python3 -m unittest test_engine.py
```

## 🗺 Project Documentation

- **[Project Vision](./vision.md)**: The high-level "why" and the fundamental requirements of the app.
- **[Implementation Roadmap](./implementation.md)**: The technical plan, including the "Walking Skeleton" and the move toward a mobile-first UI.

## 🏗 Project Structure

- `engine.py`: The core calculation engine.
- `constants.py`: Contains the Ozone Reflex 2026 wind ranges and estimation parameters.
- `test_engine.py`: Automated integration and unit tests.
- `vision.md`: Product vision and requirements.
- `implementation.md`: Development roadmap.

---
*Note: The Flask web interface is currently in development as part of the implementation roadmap.*
