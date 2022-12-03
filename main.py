from flask import Flask, request

from config.config import health_check_response
from services.register import register_discord_id

app = Flask(__name__)


@app.route("/")
def health_check():
    return health_check_response, 200


@app.route("/register", methods=["POST"])
def register():
    address = request.json["address"]
    discord_id = request.json["discordId"]
    if address == "" or discord_id == "":
        return {}, 400
    register_discord_id(address, discord_id)
    return {}, 200
