import json

from sqlalchemy.ext.declarative import DeclarativeMeta


class JsonEncoder(json.JSONEncoder):

    # @staticmethod
    # def to_dict(obj):
    #     if isinstance(obj.__class__, DeclarativeMeta):
    #         # an SQLAlchemy class
    #         fields = {}
    #         for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
    #             data = obj.__getattribute__(field)
    #             if data is not None:
    #                 try:
    #                     json.dumps(data)  # this will fail on non-encodable values, like other classes
    #                     fields[field] = data
    #                 except TypeError:
    #                     pass
    #         return fields
    #     else:
    #         return {}

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return JsonEncoder.to_dict(obj)
        return json.JSONEncoder.default(self, obj)

    @staticmethod
    def to_json(object_to_convert):
        return json.dumps(object_to_convert, cls=JsonEncoder)

    @staticmethod
    def dict_to_json(dictionary):
        return json.dumps(dictionary)
