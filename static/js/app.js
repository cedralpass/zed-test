document.addEventListener('DOMContentLoaded', () => {
    const windSpeedInput = document.getElementById('wind_speed');
    const weightInput = document.getElementById('rider_weight');
    const windSpeedLabel = document.getElementById('wind_speed_label');
    const weightLabel = document.getElementById('weight_label');
    
    const windToggle = document.getElementById('wind-speed-toggle');
    const weightToggle = document.getElementById('weight-toggle');

    if (!windSpeedInput || !weightInput || !windSpeedLabel || !weightLabel || !windToggle || !weightToggle) {
        console.error('Required elements not found in DOM');
        return;
    }

    let windUnit = 'knots'; // 'knots' or 'mph'
    let weightUnit = 'lbs'; // 'lbs' or 'kg'

    windToggle.addEventListener('click', () => {
        if (windUnit === 'knots') {
            // Switch to mph
            const val = parseFloat(windSpeedInput.value);
            if (!isNaN(val)) {
                windSpeedInput.value = (val * 1.15078).toFixed(1);
            }
            windUnit = 'mph';
            windSpeedLabel.textContent = 'Wind Speed (mph)';
            windToggle.textContent = 'MPH';
            windToggle.classList.replace('bg-blue-600', 'bg-gray-200');
            windToggle.classList.replace('text-white', 'text-gray-800');
            windToggle.classList.replace('hover:bg-blue-700', 'hover:bg-gray-300');
        } else {
            // Switch to knots
            const val = parseFloat(windSpeedInput.value);
            if (!isNaN(val)) {
                windSpeedInput.value = (val / 1.15078).toFixed(1);
            }
            windUnit = 'knots';
            windSpeedLabel.textContent = 'Wind Speed (knots)';
            windToggle.textContent = 'Knots';
            windToggle.classList.replace('bg-gray-200', 'bg-blue-600');
            windToggle.classList.replace('text-gray-800', 'text-white');
            windToggle.classList.replace('hover:bg-gray-300', 'hover:bg-blue-700');
        }
    });

    weightToggle.addEventListener('click', () => {
        if (weightUnit === 'lbs') {
            // Switch to kg
            const val = parseFloat(weightInput.value);
            if (!isNaN(val)) {
                weightInput.value = (val * 0.453592).toFixed(1);
            }
            weightUnit = 'kg';
            weightLabel.textContent = 'Rider Weight (kg)';
            weightToggle.textContent = 'Kg';
            weightToggle.classList.replace('bg-blue-600', 'bg-gray-200');
            weightToggle.classList.replace('text-white', 'text-gray-800');
            weightToggle.classList.replace('hover:bg-blue-700', 'hover:bg-gray-300');
        } else {
            // Switch to lbs
            const val = parseFloat(weightInput.value);
            if (!isNaN(val)) {
                weightInput.value = (val / 0.453592).toFixed(1);
            }
            weightUnit = 'lbs';
            weightLabel.textContent = 'Rider Weight (lbs)';
            weightToggle.textContent = 'Lbs';
            weightToggle.classList.replace('bg-gray-200', 'bg-blue-600');
            weightToggle.classList.replace('text-gray-800', 'text-white');
            weightToggle.classList.replace('hover:bg-gray-300', 'hover:bg-blue-700');
        }
    });
});
