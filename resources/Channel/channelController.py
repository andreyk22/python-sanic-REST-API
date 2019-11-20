from sanic.response import json
from bson.json_util import dumps, loads, ObjectId
from resources.Channel.channelService import get_channels, create, get_channel, update, \
    delete


async def get_all_channels():
    try:
        response = await get_channels()
        final = loads(dumps(response))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def get_single_existing_channel(channel_id):
    try:
        if not ObjectId.is_valid(channel_id):
            return {"error": "ObjectId is not valid"}

        channel = await get_channel(channel_id)
        final = loads(dumps(channel))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def add_new_channel(data):
    try:
        inserted = await create(data)
        insert_object = await get_channel(inserted.inserted_id)
        final = loads(dumps(insert_object))
        return final
    except Exception as error:
        return json({"error": error})


async def edit_existing_channel(data, channel_id):
    try:
        if not ObjectId.is_valid(channel_id):
            return {"error": "ObjectId is not valid"}

        edited_object = await update(data, channel_id)
        final = loads(dumps(edited_object))
        return final
    except Exception as error:
        return json({"error": error})


async def delete_one_channel(channel_id):
    try:
        if not ObjectId.is_valid(channel_id):
            return {"error": "ObjectId is not valid"}

        await delete(channel_id)
        return json({"message": "Channel successfully deleted."}, status=200)
    except Exception as error:
        return json({"error": error})
