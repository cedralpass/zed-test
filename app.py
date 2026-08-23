from flask import Flask, render_template, request
from engine import get_kite_size

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            # Extract and convert inputs
            wind_speed = float(request.form.get('wind_speed', 0))
            rider_weight = float(request.form.get('rider_weight', 0))
            board_type = request.form.get('board_type', 'twintip')
            
            # Perform calculation
            result = get_kite_size(wind_speed, rider_weight, board_type)
            
            # Simple error handling for extreme wind as per vision/implementation
            if wind_speed > 35:
                error = "Warning: Extreme wind speed! Be careful."
                
        except ValueError:
            error = "Please enter valid numeric values for wind speed and weight."
        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
