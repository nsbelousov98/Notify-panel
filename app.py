from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route("/", methods=["GET"])
def home():
    return "🟢 Уведомления-панель работает!"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    messages.append(data)
    return {"status": "ok"}

@app.route("/get_messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
