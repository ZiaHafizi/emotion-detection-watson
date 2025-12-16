from flask import Flask, request, jsonify
from emotion_detector import emotion_detector

# تعریف اپلیکیشن Flask
app = Flask(__name__)

# مسیر API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data or not data["text"]:
        return jsonify({"error": "Text input is required"}), 400

    text = data["text"]
    result = emotion_detector(text)
    return jsonify(result)

# اجرای سرور
if __name__ == "__main__":
    app.run(debug=True)
