def cond(troom: int, tcond: int, r: str) -> int:
    if (r == 'freeze' and troom >= tcond) or (r == 'heat' and troom <= tcond):
        return tcond
    if (r == 'heat' and troom > tcond) or (r == 'freeze' and troom < tcond):
        return troom
    if r == 'auto':
        return tcond
    if r == 'fan':
        return troom


if __name__ == '__main__':
    assert cond(10, 20, 'heat') == 20
    assert cond(10, 20, 'freeze') == 10
