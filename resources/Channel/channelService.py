from bson import ObjectId
from bson.json_util import loads

from resources.Database.db import get_mongo_connection
from resources.Database.models import ChannelModel

db = get_mongo_connection()
Channel = db.Sanic.channels


async def get_channels():
    return Channel.find({}, {"_id": 0})


async def create(body):
    body_unicode = body.decode('utf-8')
    data = loads(body_unicode)
    subs_data = []
    if "subscribers" in data:
        subs_data = data["subscribers"]

    channel_object = ChannelModel(title=data["title"], url=data["url"], subscribers=subs_data).to_mongo()
    return Channel.insert_one(channel_object)


async def get_channel(channel_id):
    return Channel.find({"_id": ObjectId(str(channel_id))}, {"_id": 0})


async def update(body, channel_id):
    body_unicode = body.decode('utf-8')
    data = loads(body_unicode)
    Channel.find_one_and_update({"_id": ObjectId(str(channel_id))}, {"$set": data})
    return Channel.find({"_id": ObjectId(str(channel_id))}, {"_id": 0})


async def delete(channel_id):
    Channel.delete_one({"_id": ObjectId(str(channel_id))})
