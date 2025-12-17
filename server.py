"""
Flask server for emotion detection API.
Provides an endpoint to predict emotions from input text.
"""

from flask import Flask, request, jsonify
from emotion_detector import emotion_detector

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict emotions from the provided text input.

    Returns:
        JSON response containing emotion scores or error message.
    """
    data = request.get_json()
    if not data or "text" not in data or not data["text"]:
        return jsonify({"error": "Text input is required"}), 400

    text = data["text"]
    result = emotion_detector(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
