def check_seq(s):
    s = s.split()
    f = True
    key = s[0]
    for i in s[1:]:
        if i > key:
            key = i
        else:
            f = False
    return 'YES' if f else 'NO'


if __name__ == '__main__':
    assert check_seq('1 7 9') == 'YES'
    assert check_seq('1 9 7') == 'NO'
    assert check_seq('2 2 2') == 'NO'
