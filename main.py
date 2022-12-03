from flask import Flask, request

from bot.eth_speaker import bot
from config.config import health_check_response, bot_token
from services.register import register_discord_id
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bot.run(bot_token)

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
