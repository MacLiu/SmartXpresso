from flask import Flask, request
from flask_pymongo import PyMongo

# Configurations
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SmartXpresso'
mongo = PyMongo(app)

# Contants
CONST_MINIMUM_TEMP_TYPE = "Minimum";
CONST_MAXIMUM_TEMP_TYPE = "Maximum";
CONST_SET_TEMP_TYPE = "Set";


# Route for GET and POST to our set temperature.
@app.route('/set-temperature', methods=['GET', 'POST'])
def set_temperature():
    if request.method == 'POST':
        temperature = request.json['temperature'];
        update_temperature(CONST_SET_TEMP_TYPE, temperature);
        return str(temperature);
    else:
        temperature = get_temperature(CONST_SET_TEMP_TYPE);
        return str(temperature);
    #endif
#enddef

# Route for GET and POST our minimum temperature.
@app.route('/min-temperature', methods=['GET', 'POST'])
def temperature_min():
    if request.method == 'POST':
        min_temperature = request.json["min-temperature"];
        update_temperature(CONST_MINIMUM_TEMP_TYPE, min_temperature);
        return str(min_temperature);
    else:
        min_temperature = get_temperature(CONST_MINIMUM_TEMP_TYPE);
        return str(min_temperature);
    #endif
#enddef

# Route for GET and POST our maximum temperature.
@app.route('/max-temperature', methods=['GET', 'POST'])
def temperature_max():
    if request.method == 'POST':
        max_temperature = request.json['max-temperature'];
        update_temperature(CONST_MAXIMUM_TEMP_TYPE, max_temperature);
        return str(max_temperature);
    else:
        max_temperature = get_temperature(CONST_MAXIMUM_TEMP_TYPE)
        return str(max_temperature);
    #endif
#enddef

############################## --- Helper Functions --- ###################################

# UPDATE temperature in Temperature Table of the according type.
def update_temperature(type, temperature):
    mongo.db.Temperature.update_one({"type": type}, {
        "$set": {
            "temperature": temperature
        }
    });
#enddef

# GET temperature in the Temperature Table for the type provided.
def get_temperature(type):
    temperature_object = mongo.db.Temperature.find({'type' : type});

    # Only one enitity in Temperature Table, so we get the first element.
    return temperature_object[0]['temperature'];
#enddef
