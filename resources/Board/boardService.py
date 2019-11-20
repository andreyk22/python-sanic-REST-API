from bson import ObjectId
from bson.json_util import loads
from datetime import date

from resources.Database.db import get_mongo_connection
from resources.Database.models import BoardModel

db = get_mongo_connection()
Board = db.Sanic.boards


async def get_boards():
    return Board.find({}, {"_id": 0})


async def create(body):
    body_unicode = body.decode('utf-8')
    data = loads(body_unicode)
    board_object = BoardModel(
        title=data["title"],
        channel_id=data["channel_id"],
        createdDate=date.today().isoformat()
    ).to_mongo()
    return Board.insert_one(board_object)


async def get_board(channel_id):
    return Board.find({"_id": ObjectId(str(channel_id))}, {"_id": 0})


async def get_boards_by_channel_id(channel_id):
    return Board.find({"channel_id": channel_id}, {"_id": 0})


async def update(body, channel_id):
    body_unicode = body.decode('utf-8')
    data = loads(body_unicode)
    Board.find_one_and_update({"_id": ObjectId(str(channel_id))}, {"$set": data})
    return Board.find({"_id": ObjectId(str(channel_id))}, {"_id": 0})


async def delete(channel_id):
    Board.delete_one({"_id": ObjectId(str(channel_id))})
