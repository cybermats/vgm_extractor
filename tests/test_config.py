import json
from unittest import TestCase

from vgm.ym2151.config import BaseConfig, ConfigEncoder


class TestConfigEncoder(TestCase):
    def test_default(self):
        class Foo:
            def __init__(self):
                self.Bar = 0

            def repr_json(self):
                return self.__dict__

        f = Foo()
        actual = json.dumps(f.repr_json(), cls=ConfigEncoder)
        expected = '{"Bar": 0}'
        self.assertEqual(actual, expected)

    def test_default_nested(self):
        class Foo:
            def __init__(self):
                self.Bar = 0

            def repr_json(self):
                return self.__dict__

        class Zoo:
            def __init__(self):
                self.foo = Foo()

            def repr_json(self):
                return self.__dict__

        z = Zoo()
        actual = json.dumps(z.repr_json(), cls=ConfigEncoder)
        expected = '{"foo": {"Bar": 0}}'
        self.assertEqual(actual, expected)
