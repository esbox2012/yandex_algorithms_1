import pytest

from lecture_3.G3 import count_honest_turtles


def test_count_honest_turtles():
    assert count_honest_turtles(['1 1', '2 0', '0 2'], 3) == 3
    assert count_honest_turtles(['1 1', '2 1', '1 2'], 3) == 1
    assert count_honest_turtles(['1 1', '1 1', '1 1'], 3) == 1
    with pytest.raises(TypeError):
        count_honest_turtles(['1 1', '0 2', '2 0'], 'ABC')


if __name__ == '__main__':
    pytest.main()
