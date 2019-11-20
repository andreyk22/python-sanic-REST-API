from sanic import Blueprint
from sanic.response import json

from resources.Message.messageController import get_messages_collection, get_board_msgs, get_single_msg, post_new_msg, \
    delete_one_message

message_blueprint = Blueprint("message", __name__)


# MESSAGE ROUTES
@message_blueprint.route("/", methods=["GET"])
async def get_all_messages(req):
    try:
        if "board" in req.args:
            by_board = await get_board_msgs(req.args["board"][0])
            return json(by_board, status=200)

        res = await get_messages_collection()
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@message_blueprint.route('/<message_id>', methods=["GET"])
async def get_single_message(req, message_id):
    try:
        res = await get_single_msg(message_id)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error})


@message_blueprint.route('/', methods=["POST"])
async def post_new_message(req):
    try:
        res = await post_new_msg(req.body)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error})


@message_blueprint.route('/<message_id>', methods=["DELETE"])
def delete_single_message(req, message_id):
    try:
        return delete_one_message(message_id)
    except Exception as error:
        return json({"message": error}, status=500)
