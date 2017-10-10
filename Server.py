from flask import Flask, request
app = Flask(__name__)

# Route for GET and POST to our set temperature.
@app.route('/set-temperature', methods=['GET', 'POST'])
def set_temperature():
    if request.method == 'POST':
        temperature = request.form['temperature'];
        # Write to our persistence what the set temperature it
        return str(temperature);
    else:
        temperature = get_set_temperature();
        return str(temperature);
    #endif
#enddef

# Route for GET and POST our minimum temperature.
@app.route('/min-temperature', methods=['GET', 'POST'])
def temperature_min():
    if request.method == 'POST':
        min_temperature = request.form['min-temperature'];
        # Write to our persistence what the set temperature it
        return str(min_temperature);
    else:
        min_temperature = get_min_temperature();
        return str(min_temperature);
    #endif
#enddef

# Route for GET and POST our maximum temperature.
@app.route('/max-temperature', methods=['GET', 'POST'])
def temperature_max():
    if request.method == 'POST':
        max_temperature = request.form['max-temperature'];
        # Write to our persistence what the set temperature it
        return str(max_temperature);
    else:
        max_temperature = get_max_temperature();
        return str(max_temperature);
    #endif
#enddef

############################## --- Helper Functions --- ###################################

# Get set temperature for the machine.
def get_set_temperature():
    return 200;
#enddef

# Get the minimum temperature for the machine.
def get_min_temperature():
    return 180;
#enddef

# Get the maximum temperature for the machine.
def get_max_temperature():
    return 300;
#enddef
