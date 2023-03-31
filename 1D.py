from typing import Union


def solve(coef: str) -> Union[str, int]:
    a, b, c = list(map(int, coef.split('\n')))
    if c < 0:
        return 'NO SOLUTION'
    elif a == 0:
        return 'NO SOLUTION' if b != c ** 2 else 'MANY SOLUTIONS'
    elif ((c ** 2 - b) / a) % 1 > 0:
        return 'NO SOLUTION'
    else:
        return (c ** 2 - b) // a


if __name__ == '__main__':
    assert (solve('1\n0\n0')) == 0
    assert (solve('1\n2\n3')) == 7
    assert (solve('1\n2\n-3')) == 'NO SOLUTION'