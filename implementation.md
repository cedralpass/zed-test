# Implementation Roadmap: Wind Kite Picker App

## Goal
To build a lightweight, "zero-build," and mobile-first web application that helps kite surfers select the optimal kite size based on wind speed, rider weight, and board type.

## Tech Stack
- **Backend**: Python 3.x with **Flask** (Minimal dependencies).
- **Frontend**: **HTML5** with **Tailwind CSS via CDN** (Zero-config styling).
- **Interactivity**: **Vanilla JavaScript** (No heavy frameworks like React/Vue).
- **Architecture**: "Walking Skeleton" approach—moving from a functional core to a polished UI.

---

## Phase 1: The Walking Skeleton (Backend & Basic UI)
*Focus: Establishing the end-to-end data flow from user input to calculation result.*

### 1.1 Flask Server (`app.py`)
- Implement a single route (`/`) handling both `GET` (displaying the form) and `POST` (processing the calculation).
- Integrate with `engine.py` to process `wind_speed`, `rider_weight`, and `board_type`.
- Pass the calculated kite size and error states (e.g., wind too high) back to the template.

### 1.2 Basic Template (`templates/index.html`)
- Create a fundamental HTML structure.
- Implement a standard HTML `<form>` with numeric inputs.
- Use Tailwind CSS to display the result in a large, readable format.

### 1.3 Testing & Validation (Phase 1)
- **End-to-End Test**: Verify that a `POST` request to `/` with sample wind/weight data correctly returns the calculated kite size in the HTML response.

### 1.4 Project Scaffolding
- Organize the directory structure:
  ```text
  ├── app.py
  ├── constants.py
  ├── engine.py
  ├── test_engine.py
  ├── templates/
  │   └── index.html
  ├── static/
  │   └── js/ (for future JS logic)
  └── .gitignore
  ```

---

## Phase 2: The UX Polish (Mobile-First & Unit Toggling)
*Focus: Optimizing for usability in high-glare, high-moisture, "at-the-beach" environments.*

### 2.1 Unit Toggling (The "Magic" Step)
- **Vanilla JS Implementation**: Add a lightweight script to handle unit switching without page re-loads.
- **Functional Requirements**:
    - Toggle between **Knots $\leftrightarrow$ MPH**.
    - Toggle between **Lbs $\leftrightarrow$ Kg**.
    - Update input labels and placeholder values dynamically.

### 2.2 Beach-Ready UI/UX
- **High-Visibility Design**: Use high-contrast Tailwind classes (e.g., deep blacks and bright whites) to ensure readability in direct sunlight.
- **Large Touch Targets**: Ensure all buttons, checkboxes, and input fields are sized for "salty finger" usability (large, easy-to-tap areas).
- **Responsive Layout**: Ensure a vertical, single-column layout that fills the mobile viewport perfectly.

### 2.3 Testing & Validation (Phase 2)
- **Unit Logic Test**: Verify via browser console or simple DOM testing that toggling between Knots/MPH and Lbs/Kg updates the UI labels and input values correctly without a page reload.
- **Visual Regression/UX Test**: Manual verification of high-contrast visibility and touch-target size on mobile viewport simulations.
