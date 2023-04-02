def metro(s: str) -> str:
    a, b, n, m = list(map(int, s.split('\n')))
    l1, l2 = [n + (n - 1) * a, n + (n + 1) * a], [m + (m - 1) * b, m + (m + 1) * b]
    res = -1
    if l1[0] < l2[1] and l1[1] > l2[0]:
        res = [max(l1[0], l2[0]), min(l1[1], l2[1])]
    elif l1[0] == l2[1]:
        res = [l1[0], l1[0]]
    elif l1[1] == l2[0]:
        res = [l2[0], l2[0]]
    return ' '.join(list(map(str, res))) if res != -1 else str(res)


if __name__ == '__main__':
    assert metro('1\n3\n3\n2') == '5 7'
    assert metro('1\n5\n1\n2') == '-1'
