def find_max_pair_product(sequence: list) -> tuple:
    min_negative = max_positive = max(sequence[0], sequence[1])
    max_negative = min_positive = min(sequence[0], sequence[1])
    for number in sequence[2:]:
        if number > max_positive:
            max_positive, min_positive = number, max_positive
        elif number > min_positive:
            min_positive = number
        elif number < max_negative:
            max_negative, min_negative = number, max_negative
        elif number < min_negative:
            min_negative = number
    return (max_negative, min_negative) if min_negative * max_negative > min_positive * max_positive else (
        min_positive, max_positive)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        sequence_ = list(map(int, reader.read().rstrip().split()))

    print(*find_max_pair_product(sequence_))

    assert find_max_pair_product([4, 3, 5, 2, 5]) == (5, 5)
    assert find_max_pair_product([-4, 3, -5, 2, 5]) == (-5, -4)
