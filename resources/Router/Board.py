from sanic import Blueprint
from sanic.response import json

from resources.Board.boardController import get_all_boards, get_single_existing_board, add_new_board, \
    edit_existing_board, delete_existing_board, get_boards_by_channel

board_blueprint = Blueprint("board", __name__)


# BOARD ROUTES
@board_blueprint.route("/", methods=["GET"])
async def get_boards(req):
    try:
        if "channel" in req.args:
            by_channel = await get_boards_by_channel(req.args["channel"][0])
            return json(by_channel, status=200)

        res = await get_all_boards()
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@board_blueprint.route("/<board_id>", methods=["GET"])
async def get_single_board(req, board_id):
    try:
        res = await get_single_existing_board(board_id)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@board_blueprint.route("/", methods=["POST"])
async def create_new_board(req):
    try:
        res = await add_new_board(req.body)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@board_blueprint.route("/<board_id>", methods=["PUT"])
async def edit_board(req, board_id):
    try:
        res = await edit_existing_board(req.body, board_id)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@board_blueprint.route("/<board_id>", methods=["DELETE"])
async def delete_board(req, board_id):
    try:
        res = await delete_existing_board(board_id)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)
