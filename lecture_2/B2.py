def d(s: list) -> list:
    res = []
    for i in range(1, len(s)):
        if s[i] == -2000000000:
            break
        elif s[i] > s[i - 1]:
            res.append(2)
        elif s[i] == s[i - 1] and s[i] > s[0]:
            res.append(1)
        elif s[i] == s[i - 1] and s[i] < s[0]:
            res.append(-1)
        elif s[i] == s[i - 1]:
            res.append(0)
        elif s[i] < s[i - 1]:
            res.append(-2)
    return res


def seq(s: str) -> str:
    s = list(map(int, s.split('\n')))
    if len(s) == 1 or len(s) == 2:
        return 'CONSTANT'
    else:
        s = list(set(d(s)))
        if len(s) == 1:
            return {2: 'ASCENDING', 0: 'CONSTANT', -2: 'DESCENDING'}[s[0]]
        elif len(s) == 2:
            if (s[0] == 2 and s[1] == 1) or (s[0] == 1 and s[1] == 2):
                return 'WEAKLY ASCENDING'
            elif (s[0] == -2 and s[1] == -1) or (s[0] == -1 and s[1] == -2):
                return 'WEAKLY DESCENDING'
            elif (s[0] == 0 and s[1] == 2) or (s[0] == 2 and s[1] == 0):
                return 'WEAKLY ASCENDING'
            elif (s[0] == 0 and s[1] == -2) or (s[0] == -2 and s[1] == 0):
                return 'WEAKLY DESCENDING'
            else:
                return 'RANDOM'
        else:
            return 'RANDOM'


if __name__ == '__main__':
    assert seq('-530\n-530\n-530\n-530\n-530\n-530\n-2000000000') == 'CONSTANT'
