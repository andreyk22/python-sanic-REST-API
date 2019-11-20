from sanic.response import json
from bson.json_util import dumps, loads
from resources.Message.messageService import get_message, get_all_messages, get_messages_by_board, post_message, \
    delete_message

from bson.json_util import ObjectId


async def get_messages_collection():
    try:
        response = await get_all_messages()
        final = loads(dumps(response))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def get_single_msg(message_id):
    try:
        if not ObjectId.is_valid(message_id):
            return {"error": "ObjectId is not valid"}

        message = await get_message(message_id)
        final = loads(dumps(message))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def get_board_msgs(board_id):
    try:
        if not ObjectId.is_valid(board_id):
            return {"error": "ObjectId is not valid"}
        messages = await get_messages_by_board(board_id)
        final = loads(dumps(messages))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def post_new_msg(data):
    try:
        inserted = await post_message(data)
        insert_object = await get_message(inserted.inserted_id)
        final = loads(dumps(insert_object))
        return final
    except Exception as error:
        return json({"error": error})


async def delete_one_message(message_id):
    try:
        if not ObjectId.is_valid(message_id):
            return {"error": "ObjectId is not valid"}

        await delete_message(message_id)
        return json({"message": "Channel successfully deleted."}, status=200)
    except Exception as error:
        return json({"error": error})
