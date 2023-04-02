def solve(s: str) -> str:
    a, b, c, d, e, f = list(map(float, s.split('\n')))
    if c != 0 and d != 0 and a / c == b / d:
        if f != 0 and b / d == e / f:
            return f'1 {-c / d} {f / d}'
        if f == 0 and e == 0:
            return f'1 1 0'
        elif b / d != e / f:
            return '0'
    elif c == d == f == 0 and a != 0 and b != 0 and e != 0:
        return f'1 {-a / b} {e / b}'
    elif (a == b == c == d == 0 and (e != 0 or f != 0)) or (
            c != 0 and d != 0 and f != 0 and a / c == b / d and b / d != e / f):
        return '0'
    elif a == b == c == d == e == f == 0:
        return '5'
    elif b == 0 and d == 0:
        if c != 0 and f != 0 and a / c != e / f:
            return '0'
        else:
            if a == 0 and e == 0:
                return f'3 {f / c}'
            else:
                return f'3 {e / a}'
    elif a == 0 and c == 0:
        if (e == 0 and f != 0 and b != 0) or (e != 0 and f == 0 and d != 0):
            return '0'
        elif b == 0:
            return f'4 {f / d}'
        else:
            return f'4 {e / b}'
    elif a == d == 0 and c != 0 and b != 0:
        x0 = f / c
        y0 = e / b
        return f'2 {x0} {y0}'
    elif b == c == 0 and a != 0 and d != 0:
        x0 = e / a
        y0 = f / d
        return f'2 {x0} {y0}'
    else:
        y0 = (a * f - c * e) / (a * d - c * b)
        x0 = (e - b * y0) / a
        return f'2 {x0} {y0}'


if __name__ == '__main__':
    assert solve('1\n0\n0\n1\n3\n3') == '2 3.0 3.0'
    assert solve('1\n1\n2\n2\n1\n2') == '1 -1.0 1.0'
    assert solve('0\n2\n0\n4\n1\n2') == '4 0.5'
