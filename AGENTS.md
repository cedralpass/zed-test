# Agent Instructions for Wind Kite Picker

## 🎯 Project Overview
The **Wind Kite Picker App** is a lightweight, mobile-first web application designed to help kite surfers select the optimal kite size based on real-time wind speed, rider weight, and board type.

The app uses two primary methods:
1. **Ozone Reflex 2026 "Sweetspot" Lookup**: Uses authoritative manufacturer data for optimal wind ranges.
2. **Estimation Fallback**: A mathematical model (15kt/15m baseline) for quick recommendations when specific data is unavailable.

## 🛠 Tech Stack & Architecture
- **Backend**: Python 3.13 with **Flask** (minimal dependencies).
- **Frontend**: **HTML5** with **Tailwind CSS** (via CDN) and **Vanilla JavaScript** (zero-dependency, instant interactivity).
- **Core Logic**: Python-based calculation engine (`engine.py`) and constants (`constants.py`).
- **Environment Management**: **`uv`** is the primary tool for dependency and Python version management.

## 🚀 Development Workflow
- **Environment**: Always use the virtual environment managed by `uv` located at `./.venv`.
- **Dependencies**: Managed via `pyproject.toml` and `uv.lock`.
- **Python Version**: Python 3.13 (pinned via `.python-version`).

## 🧪 Testing Protocol
- **Framework Preference**: We prefer **`pytest`** over `unittest`.
- **Running Pytest**: ALWAYS execute tests using the local virtual environment binary to avoid `uv` cache permission errors.
  - Use: `./.venv/bin/pytest`
  - **NEVER** use: `uv run pytest`

## 🎨 Design Principles (Beach-Ready UI)
- **Mobile-First**: Optimized for one-handed use on a smartphone at the beach.
- **High Contrast/Visibility**: Large touch targets and clear typography for use in bright, sunny, high-glare environments.
- **Zero-Dependency UI**: Avoid heavy JS frameworks (React/Vue) to keep "Time to Interactive" near-instant.
- **Unit Toggling**: Smoothly switch between Knots $\leftrightarrow$ MPH and Lbs $\leftrightarrow$ Kg via Vanilla JS.
