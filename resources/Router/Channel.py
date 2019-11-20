from sanic import Blueprint
from sanic.response import json

from resources.Channel.channelController import get_all_channels, get_single_existing_channel, add_new_channel, \
    edit_existing_channel, delete_one_channel

channel_blueprint = Blueprint("channel", __name__)


# Channel routes
@channel_blueprint.route("/", methods=["GET"])
async def get_channels(req):
    try:
        res = await get_all_channels()
        return json(res, status=200)
    except Exception as error:
        print(error)
        return json({"message": error}, status=500)


@channel_blueprint.route("/<channel_id>", methods=["GET"])
async def get_single_channel(req, channel_id):
    try:
        res = await get_single_existing_channel(channel_id)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@channel_blueprint.route("/", methods=["POST"])
async def create_new_channel(req):
    try:
        res = await add_new_channel(req.body)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@channel_blueprint.route("/<channel_id>", methods=["PUT"])
async def edit_channel(req, channel_id):
    try:
        res = await edit_existing_channel(req.body, channel_id)
        return json(res, status=200)
    except Exception as error:
        return json({"message": error}, status=500)


@channel_blueprint.route("/<channel_id>", methods=["DELETE"])
def delete_channel(req, channel_id):
    try:
        return delete_one_channel(channel_id)
    except Exception as error:
        return json({"message": error}, status=500)
