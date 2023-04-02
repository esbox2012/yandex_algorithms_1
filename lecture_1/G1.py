def details(s: str) -> int:
    n, k, m = list(map(int, s.split()))
    count = 0
    while n >= k:
        if k // m == 0:
            break
        count += k // m
        n -= k
        n += k % m
    return count


if __name__ == '__main__':
    assert details('10 5 2') == 4
    assert details('13 5 3') == 3
    assert details('14 5 3') == 4
