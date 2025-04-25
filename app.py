from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model once when the app starts
model = joblib.load("salary_predict_model.ml")


@app.route("/")
def home():
    """Landing page for the Salary Prediction API"""
    return (
        "<h1>Salary Prediction API</h1>"
        "<p>BAIS:3300 - Digital Product Development</p>"
        "<p>Emma Chase</p>"
    )


@app.route("/predict", methods=["GET"])
def predict():
  return "<h1>Prediction route is working...</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
