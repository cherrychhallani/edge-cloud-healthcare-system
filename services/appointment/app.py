import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
appointments = []

@app.route('/')
def home():
    return "Appointment Service Running"

# Create appointment
@app.route('/appointment', methods=['POST'])
def create_appointment():
    data = request.json
    
    appointment = {
        "id": len(appointments) + 1,
        "name": data.get("name"),
        "age": data.get("age"),
        "problem": data.get("problem")
    }
    
    appointments.append(appointment)

    # Send to Gateway
    try:
        response = requests.post(
            "http://gateway:5002/process",
            json=appointment
        )
        gateway_response = response.json()
    except Exception as e:
        gateway_response = {"error": str(e)}

    return jsonify({
        "message": "Appointment created",
        "appointment": appointment,
        "gateway_response": gateway_response
    })

# Get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
