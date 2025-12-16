from flask import Flask, request, jsonify
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    result = emotion_detector(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
