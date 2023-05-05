def elements_counter(sequence: list) -> int:
    return len(set(sequence))


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        sequence_ = reader.read().rstrip().split()

    print(elements_counter(sequence_))

    assert elements_counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert elements_counter([1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]) == 6
