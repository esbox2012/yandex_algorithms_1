import math


def ambulance(s: str) -> str:
    p, n = set(), set()
    k1, m, k2, p2, n2 = list(map(int, s.split()))
    totalm = (p2 - 1) * m + n2
    ans = []
    for i in range(1, 1000000):
        totali = math.ceil(k2 / i)
        if totali == totalm:
            ans.append(i)
        if len(ans) > 10: break
    if ans == [] or n2 > m:
        return '-1 -1'
    elif len(ans) == 1:
        p1 = math.ceil(k1 / ans[0] / m)
        n1 = math.ceil(k1 / ans[0] - m * (p1 - 1))
        return f'{p1} {n1}'
    elif len(ans) > 1:
        for i in ans:
            p1 = math.ceil(k1 / i / m)
            p.add(p1)
            n1 = math.ceil(k1 / i - m * (p1 - 1))
            n.add(n1)
        if len(p) > 1:
            p1 = 0
        else:
            p1 = list(p)[0]
        if len(n) > 1:
            n1 = 0
        else:
            n1 = list(n)[0]
        return f'{p1} {n1}'


if __name__ == '__main__':
    assert ambulance('89 20 41 1 11') == '2 3'
    assert ambulance('11 1 1 1 1') == '0 1'
    assert ambulance('3 2 2 2 1') == '-1 -1'
