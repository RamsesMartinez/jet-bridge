import json

from jet_bridge.fields.field import Field


class JSONField(Field):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_internal_value(self, value):
        return json.loads(value)

    def to_representation(self, value):
        return value