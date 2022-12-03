from flask import Flask

from server.config.config import health_check_response

app = Flask(__name__)


@app.route("/")
def health_check():
    return health_check_response, 200
