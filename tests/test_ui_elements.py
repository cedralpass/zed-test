import pytest

def test_unit_toggles_exist():
    # We can use the existing test_app.py logic or just mock the HTML
    html_content = """
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg p-8">
        <div id="unit-toggles" class="mb-4 flex justify-between">
            <!-- Toggles should be here -->
        </div>
        <form method="POST" class="space-y-6">
            <div>
                <label for="wind_speed" class="block text-sm font-medium text-gray-700 mb-1">Wind Speed (knots)</label>
                <input type="number" step="0.1" name="wind_speed" id="wind_speed" required
                    class="w-full px-4 py-3 rounded-md border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="e.g. 15" value="15">
            </div>
        </form>
    </div>
    """
    
    # Check for wind speed toggle button presence by ID
    assert 'id="wind-speed-toggle"' in html_content, "Wind speed toggle button not found"
    
    # Check for weight toggle button presence by ID
    assert 'id="weight-toggle"' in html_content, "Weight toggle button not found"
