
from marshmallow import Schema, fields, post_load


class WebRequest():
    def __init__(self, store_id, date):
        self.store_id = store_id
        self.date = date


class WebRequestSchema(Schema):
    store_id = fields.UUID()
    date = fields.Date()

    @post_load
    def make_web_request(self, data, **kwargs):
        return WebRequest(**data)
