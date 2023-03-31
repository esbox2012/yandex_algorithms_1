def notebook(s: str) -> str:
    a, b, c, d = map(int, s.split())
    if a == c:
        return f'{a} {b + d}'
    elif a == d:
        return f'{a} {b + c}'
    elif b == c:
        return f'{b} {a + d}'
    elif b == d:
        return f'{b} {a + c}'
    else:
        s = sorted([[a + c, max(b, d), (a + c) * max(b, d)], [a + d, max(b, c), (a + d) * max(b, c)],
                    [b + c, max(a, d), (b + c) * max(a, d)], [b + d, max(a, c), (b + d) * max(a, c)]],
                   key=lambda x: x[2])
        return f'{s[0][0]} {s[0][1]}'


if __name__ == '__main__':
    assert notebook('10 2 2 10') == '10 4'
    assert notebook('5 7 3 2') == '9 5'
