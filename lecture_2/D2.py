def counter(s: str) -> int:
    s = [int(i) for i in s.split()]
    count = 0
    for i in range(1, len(s) - 1):
        if s[i - 1] < s[i] > s[i + 1]: count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        print(counter(reader.read().rstrip()))

    assert counter('1 2 3 4 5') == 0
    assert counter('5 4 3 2 1') == 0
    assert counter('1 5 1 5 1') == 2
