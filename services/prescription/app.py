from flask import Flask, request, jsonify

app = Flask(__name__)

prescriptions = []

@app.route('/')
def home():
    return "Prescription Service Running"

@app.route('/prescription', methods=['POST'])
def create_prescription():
    data = request.json

    prescription = {
        "id": len(prescriptions) + 1,
        "patient_name": data.get("name"),
        "medicines": ["Paracetamol", "Cough Syrup"],  # static for now
        "notes": "Take rest and stay hydrated"
    }

    prescriptions.append(prescription)

    return jsonify({
        "message": "Prescription created",
        "prescription": prescription
    })

@app.route('/prescriptions', methods=['GET'])
def get_prescriptions():
    return jsonify(prescriptions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
