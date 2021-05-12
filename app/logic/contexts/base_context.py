from json import JSONEncoder


class BaseContext(JSONEncoder):
    def __init__(self):
        super(BaseContext, self).__init__()
        self.instance = None

    def __repr__(self):

        if self.instance is not None:
            return self.instance.__repr__()
        else:
            return ""

    def json(self):
        if self.instance is not None:
            return self.instance.json()
        else:
            return None
