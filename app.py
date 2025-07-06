from flask import Flask, request, jsonify, Response
import json

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
    return Response(
        json.dumps(messages, ensure_ascii=False, indent=2),
        content_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
