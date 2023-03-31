def triangle(a: int, b: int, c: int) -> str:
    s = sorted([a, b, c], reverse=True)
    return 'YES' if s[0] < s[1] + s[2] else 'NO'


if __name__ == '__main__':
    assert triangle(3, 4, 5) == 'YES'
    assert triangle(3, 5, 4) == 'YES'
    assert triangle(4, 5, 3) == 'YES'
