def find_max_three_conduct(sequence: list) -> tuple:
    min_positive, middle_positive, max_positive = max_negative, middle_negative, min_negative = sorted(sequence[:3])
    for number in sequence[3:]:
        if number > max_positive:
            max_positive, middle_positive, min_positive = number, max_positive, middle_positive
        elif number > middle_positive:
            middle_positive, min_positive = number, middle_positive
        elif number > min_positive:
            min_positive = number
        elif number < max_negative:
            max_negative, middle_negative, min_negative = number, max_negative, middle_negative
        elif number < middle_negative:
            middle_negative, min_negative = number, middle_negative
        elif number < min_negative:
            min_negative = number
    if max_negative * middle_negative * max_positive > max_positive * middle_positive * min_positive:
        return (max_negative, middle_negative, max_positive)
    else:
        return (max_positive, middle_positive, min_positive)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        sequence_ = list(map(int, reader.read().rstrip().split()))
    print(*find_max_three_conduct(sequence_))

    assert find_max_three_conduct([1, 2, 3]) == (3, 2, 1)
    assert find_max_three_conduct([-5, -30000, -12]) == (-5, -12, -30000)
