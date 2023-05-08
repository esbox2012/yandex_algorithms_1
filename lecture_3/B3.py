def find_common_sequence(a: list, b: list) -> list:
    a, b = set(a), set(b)
    if len(a) > len(b):
        a, b = b, a
    return sorted(i for i in a if i in b)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        sequence1, sequence2 = reader.read().rstrip().split('\n')
    sequence1 = [map(int, sequence1.split())]
    sequence2 = [map(int, sequence2.split())]
    print(*find_common_sequence(sequence1, sequence2))

    assert find_common_sequence([1, 3, 2], [4, 3, 2]) == [2, 3]
    assert find_common_sequence([1, 2, 6, 4, 5, 7], [10, 2, 3, 4, 8]) == [2, 4]
