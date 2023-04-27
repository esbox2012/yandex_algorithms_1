def find_missing_sequence(seq: list, num: int) -> str:
    if num == 1:
        return '0'
    for position in range(num):
        i = position
        j = num - 1
        while i < num and j > 0 and i <= j and seq[i] == seq[j]:
            i += 1
            j -= 1
        if i > j:
            missing_sequence = seq[:position][::-1]
            return f'{position}\n{" ".join(missing_sequence)}'


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        num_, seq_ = reader.read().rstrip().split('\n')
    num_ = int(num_)
    seq_ = seq_.split()
    print(find_missing_sequence(seq_, num_))

    assert find_missing_sequence(['1', '2', '3', '4', '5', '4', '3', '2', '1'], 9) == '0\n'
    assert find_missing_sequence(['1', '2', '1', '2', '2'], 5) == '3\n1 2 1'
    assert find_missing_sequence(['1', '2', '3', '4', '5'], 5) == '4\n4 3 2 1'
