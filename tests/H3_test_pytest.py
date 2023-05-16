import pytest
from lecture_3.H3 import shots


def test_shots():
    assert shots(['1 1', '2 2', '3 3']) == 3
    assert shots(['1 1', '1 2', '1 3']) == 1
    assert shots(['1 1', '2 1', '3 1']) == 3
    assert shots(['1 1', '2 1', '3 1']) == 3
    with pytest.raises(TypeError):
        shots('ABC')


if __name__ == '__main__':
    pytest.main()
