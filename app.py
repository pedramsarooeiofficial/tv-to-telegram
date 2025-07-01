from flask import Flask, request
import requests
import os

app = Flask(name)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

@app.route("/", methods=["GET"])
def home():
    return "Server is running."

@app.route("/alert", methods=["POST"])
def alert():
    data = request.get_json()
    message = data.get("message", "SQZMOM ALERT!")
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": USER_ID,
        "text": message
    }
    requests.post(url, json=payload)
    
    return "Alert sent", 200
