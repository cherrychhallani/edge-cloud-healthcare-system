import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Clinic Gateway Running"

# Receive appointment request (for now just echo)
@app.route('/process', methods=['POST'])
def process_request():
    data = request.json

    try:
        # Patient Service
        patient_res = requests.post(
            "http://127.0.0.1:5003/patient",
            json=data
        ).json()

        # Billing Service
        billing_res = requests.post(
            "http://127.0.0.1:5004/bill",
            json=data
        ).json()

        # Prescription Service
        prescription_res = requests.post(
            "http://127.0.0.1:5005/prescription",
            json=data
        ).json()

    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({
        "message": "Full system processed",
        "patient": patient_res,
        "billing": billing_res,
        "prescription": prescription_res
    })

if __name__ == '__main__':
    app.run(port=5002, debug=True)
