from mongoengine import *


class BoardModel(Document):
    __collection__ = "boards"

    title = StringField(required=True, max_length=100)
    channel_id = StringField(required=True, max_length=30)
    createdDate = StringField(required=True)


class ChannelModel(Document):
    __collection__ = "channels"

    title = StringField(required=True, max_length=100)
    url = StringField(required=True, max_length=255)
    subscribers = ListField(required=False)


class MessageModel(Document):
    __collection__ = "messages"

    board_id = StringField(required=True, max_length=30)
    message = StringField(required=True, max_length=255)
