import pytest
from lecture_3.J3 import lang


def test_lang():
    assert lang([{'English'}, {'Russian'}, {'French'}]) == (0, set(), 3, {'English', 'Russian', 'French'})
    assert lang([{'English', 'Russian'}, {'Russian', 'English'}, {'French', 'Russian'}]) == (
        1, {'Russian'}, 3, {'English', 'Russian', 'French'})
    assert lang([{'English'}, {'English'}, {'English'}]) == (1, {'English'}, 1, {'English'})
    with pytest.raises(TypeError):
        lang(3)


if __name__ == '__main__':
    pytest.main()
