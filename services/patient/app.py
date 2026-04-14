from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
patients = []

@app.route('/')
def home():
    return "Patient Record Service Running"

# Get or create patient
@app.route('/patient', methods=['POST'])
def handle_patient():
    data = request.json
    name = data.get("name")

    # Check if patient exists
    for patient in patients:
        if patient["name"] == name:
            return jsonify({
                "message": "Patient exists",
                "patient": patient
            })

    # Create new patient
    new_patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": data.get("age"),
        "history": []
    }

    patients.append(new_patient)

    return jsonify({
        "message": "New patient created",
        "patient": new_patient
    })

# Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
