import pytest
from lecture_4.A4 import find_synonym


def test_find_synonym():
    assert find_synonym(['hi bye'], 'bye') == 'hi'
    assert find_synonym(['123 456'], '123') == '456'
    with pytest.raises(ValueError):
        find_synonym(['hy bye'], '')
    with pytest.raises(TypeError):
        find_synonym(['hi bye'], 123)


if __name__ == '__main__':
    pytest.main()
