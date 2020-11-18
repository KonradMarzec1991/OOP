import pytest
from .mod import Mod


class TestModClass:

    def test_init(self):
        with pytest.raises(AttributeError):
            Mod('abc', 'abc')
            Mod('abc', 2)
            Mod(2, 'abc')
            Mod(2.5, 2.5)
