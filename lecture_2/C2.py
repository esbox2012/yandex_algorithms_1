def nearest_element(s: str) -> int:
    n, elements, x = s.split('\n')
    n, elements, x = int(n), list(map(int, elements.split())), int(x)
    result = elements[0]
    for index, value in enumerate(elements, 1):
        if abs(value - x) <= abs(result - x): result = value
    return result


if __name__ == '__main__':
    assert nearest_element('5\n1 2 3 4 5\n6') == 5
    assert nearest_element('5\n5 4 3 2 1\n3') == 3
