from datetime import date


class CardInside:
    """
    # TODO Add needed fields
    """

    def __init__(self, foreground="WordToLearn", background="Definition"):
        super(CardInside, self).__init__()
        self.foreground = foreground
        self.background = background

    def __repr__(self):
        """
        :return: Json string representing card inner body
        (foreground and background parts and contexts)
        """
        return ""

    def _to_dict(self):
        to_ret = self.__dict__.copy()
        if '_sa_instance_state' in to_ret:
            to_ret.pop('_sa_instance_state')
        return to_ret.items()

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict()
        }
