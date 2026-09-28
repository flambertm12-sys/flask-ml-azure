from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask ML app is running on Azure!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    result = {
        "input": data,
        "prediction": 42
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
