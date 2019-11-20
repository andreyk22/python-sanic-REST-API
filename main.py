from sanic import Sanic

from resources.Router.Message import message_blueprint
from resources.Router.Channel import channel_blueprint
from resources.Router.Board import board_blueprint

app = Sanic()

app.blueprint(message_blueprint, url_prefix="/message")
app.blueprint(channel_blueprint, url_prefix="/channel")
app.blueprint(board_blueprint, url_prefix="/board")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4200)
