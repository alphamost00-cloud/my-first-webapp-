from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/home", methods=["GET"])
def api_home():
    return jsonify(
        status="success",
        message="Welcome to the Flask API home endpoint.",
    )

@app.route("/api/data", methods=["GET"])
def api_data():
    sample_data = {
        "items": [
            {"id": 1, "name": "Apple", "price": 0.99},
            {"id": 2, "name": "Banana", "price": 0.59},
            {"id": 3, "name": "Cherry", "price": 2.49},
        ],
        "count": 3,
    }
    return jsonify(status="success", data=sample_data)

@app.route("/api/sum", methods=["POST"])
def api_sum():
    payload = request.get_json(silent=True) or {}
    numbers = payload.get("numbers")

    if not isinstance(numbers, list):
        return jsonify(
            status="error",
            message="Send a JSON body with a numeric list in 'numbers'.",
        ), 400

    try:
        total = sum(float(value) for value in numbers)
    except (TypeError, ValueError):
        return jsonify(
            status="error",
            message="All list items must be numbers.",
        ), 400

    return jsonify(status="success", numbers=numbers, result=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
