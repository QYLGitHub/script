# -*- coding: utf8 -*-
class BaseFields(object):

    def __init__(self, **kwargs):
        self._item = dict(kwargs)
        self._value = kwargs["value"]
        self._name = kwargs.get("name", '')
        if getattr(self, "type_", None) is None:
            raise ValueError()
        if not isinstance(self._value, self.type_):
            raise TypeError()

    def __setattr__(self, key, value):
        if key in ('_item', '_value', 'type_', '_name'):
            super(BaseFields, self).__setattr__(key, value)
            return
        if not isinstance(value, self.type_):
            raise TypeError()
        super(BaseFields, self).__setattr__(key, value)

    def __get__(self, instance, owner):
        return self._value


class Models(object):

    @staticmethod
    def to_str(value):
        return str(value)

    @staticmethod
    def to_json(value):
        if isinstance(value, dict):
            import json
            return json.dumps(value, ensure_ascii=False)
        elif isinstance(value, str):
            return value
        raise TypeError()

    @staticmethod
    def to_dict(value):
        if isinstance(value, str):
            import json
            return json.loads(value)
        raise TypeError


class IntField(BaseFields):

    def __init__(self, **kwargs):
        self.type_ = int
        super(IntField, self).__init__(**kwargs)


class StrField(BaseFields):

    def __init__(self, **kwargs):
        self.type_ = str
        super(StrField, self).__init__(**kwargs)


class DcitField(BaseFields):

    def __init__(self, **kwargs):
        self.type_ = dict
        super(DcitField, self).__init__(**kwargs)


class ListField(BaseFields):

    def __init__(self, **kwargs):
        self.type_ = list
        super(ListField, self).__init__(**kwargs)


class TupleField(BaseFields):

    def __init__(self, **kwargs):
        self.type_ = tuple
        super(TupleField, self).__init__(**kwargs)


class SetField(BaseFields):

    def __init__(self, **kwargs):
        self.type_ = set
        super(SetField, self).__init__(**kwargs)
