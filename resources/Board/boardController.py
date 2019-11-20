from sanic.response import json
from bson.json_util import dumps, loads, ObjectId

from resources.Board.boardService import get_boards, create, get_board, get_boards_by_channel_id, update, delete


async def get_all_boards():
    try:
        response = await get_boards()
        final = loads(dumps(response))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def add_new_board(data):
    try:
        inserted = await create(data)
        inserted_object = await get_board(inserted.inserted_id)
        final = loads(dumps(inserted_object))
        return final
    except Exception as error:
        return json({"error": error})


async def get_single_existing_board(board_id):
    try:
        if not ObjectId.is_valid(board_id):
            return {"error": "ObjectId is not valid"}

        response = await get_board(board_id)
        final = loads(dumps(response))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def get_boards_by_channel(channel_id):
    try:
        if not ObjectId.is_valid(channel_id):
            return {"error": "ObjectId is not valid"}

        response = await get_boards_by_channel_id(channel_id)
        final = loads(dumps(response))
        if final:
            return final
        return []
    except Exception as error:
        return json({"error": error})


async def edit_existing_board(data, board_id):
    try:
        if not ObjectId.is_valid(board_id):
            return {"error": "ObjectId is not valid"}

        response = await update(data, board_id)
        final = loads(dumps(response))
        return final
    except Exception as error:
        return json({"error": error})


async def delete_existing_board(board_id):
    try:
        if not ObjectId.is_valid(board_id):
            return {"error": "ObjectId is not valid"}

        await delete(board_id)
        return {"message": "Board successfully deleted."}
    except Exception as error:
        return json({"error": error})
