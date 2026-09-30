from flask import Flask, request, jsonify

app = Flask(__name__)

customers = []
next_id = 1


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/customers", methods=["POST"])
def register_customer():
    global next_id

    data = request.get_json()

    customer = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"]
    }

    customers.append(customer)
    next_id += 1

    return jsonify(customer), 201


@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)