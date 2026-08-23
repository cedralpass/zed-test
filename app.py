from flask import Flask, render_template, request
from engine import get_kite_size

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    wind_speed = ""
    rider_weight = ""
    board_type = "twintip"
    
    if request.method == 'POST':
        wind_speed = request.form.get('wind_speed', '')
        rider_weight = request.form.get('rider_weight', '')
        board_type = request.form.get('board_type', 'twintip')
        
        try:
            # Convert for calculation
            wind_speed_float = float(wind_speed) if wind_speed else 0.0
            rider_weight_float = float(rider_weight) if rider_weight else 0.0
            
            # Perform calculation
            result = get_kite_size(wind_speed_float, rider_weight_float, board_type)
            
            # Simple error handling for extreme wind as per vision/implementation
            if wind_speed_float > 35:
                error = "Warning: Extreme wind speed! Be careful."
                
        except ValueError:
            error = "Please enter valid numeric values for wind speed and weight."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('index.html', 
                           result=result, 
                           error=error, 
                           wind_speed=wind_speed, 
                           rider_weight=rider_weight, 
                           board_type=board_type)

if __name__ == '__main__':
    app.run(debug=True)
