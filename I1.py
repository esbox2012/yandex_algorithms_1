def castle(s: str) -> str:
    a, b, c, d, e = list(map(int, s.split('\n')))
    brick = sorted([a, b, c])
    window = sorted([d, e])
    return 'YES' if brick[0] <= window[0] and brick[1] <= window[1] else 'NO'


if __name__ == '__main__':
    assert castle('1\n1\n1\n1\n1') == 'YES'
    assert castle('2\n2\n2\n1\n1') == 'NO'
