
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

cards = []

@app.route("/")
def index():
    return render_template("index.html", cards=cards)

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    data["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cards.append(data)
    return jsonify({"status": "received"})

@app.route("/cards", methods=["GET"])
def get_cards():
    return jsonify(cards)

@app.route("/clear", methods=["POST"])
def clear():
    cards.clear()
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
