from bson import ObjectId
from bson.json_util import loads
from resources.Database.db import get_mongo_connection
from resources.Database.models import MessageModel

db = get_mongo_connection()
Message = db.Sanic.messages


async def get_all_messages():
    return Message.find({}, {"_id": 0})


async def get_messages_by_board(board_id):
    return Message.find({"board_id": board_id}, {"_id": 0})


async def get_message(message_id):
    return Message.find({"_id": ObjectId(str(message_id))}, {"_id": 0})


async def post_message(data):
    body_unicode = data.decode('utf-8')
    payload = loads(body_unicode)
    msg_object = MessageModel(board_id=payload["board_id"], message=payload["message"]).to_mongo()
    return Message.insert_one(msg_object)


async def delete_message(message_id):
    Message.delete_one({"_id": ObjectId(str(message_id))})
