from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    # We are using a placeholder model because the real model file is not available
    # This returns a fake prediction so your app works end-to-end
    placeholder_emotion = "happy"

    return jsonify({
        "emotion": placeholder_emotion
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
