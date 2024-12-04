from flask import Flask, jsonify
import math

app = Flask(__name__)

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    prime_status = prime(number)
    return jsonify({"Number": number, "isPrime": prime_status})

airports = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "KATL": {"Name": "Hartsfield-Jackson Atlanta International Airport", "Location": "Atlanta"},
}


@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport = airports.get(icao_code)
    if airport:
        return jsonify({"ICAO": icao_code, "Name": airport["Name"], "Location": airport["Location"]})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '_main_':
    app.run(debug=True)