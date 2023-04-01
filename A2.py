def check_seq(s):
    s = s.split()
    i = 1
    while i < len(s) and s[i] > s[i - 1]:
        i += 1
    return 'YES' if i == len(s) else 'NO'


if __name__ == '__main__':
    assert check_seq('1 7 9') == 'YES'
    assert check_seq('1 9 7') == 'NO'
    assert check_seq('2 2 2') == 'NO'
