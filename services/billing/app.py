from flask import Flask, request, jsonify

app = Flask(__name__)

bills = []

@app.route('/')
def home():
    return "Billing Service Running"

@app.route('/bill', methods=['POST'])
def generate_bill():
    data = request.json

    bill = {
        "id": len(bills) + 1,
        "patient_name": data.get("name"),
        "amount": 500,  # fixed for now
        "status": "unpaid"
    }

    bills.append(bill)

    return jsonify({
        "message": "Bill generated",
        "bill": bill
    })

@app.route('/bills', methods=['GET'])
def get_bills():
    return jsonify(bills)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
