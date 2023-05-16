def shots(birds: list) -> int:
    if not isinstance(birds, list):
        raise TypeError('Use list')
    number_shots = set([bird.split()[0] for bird in birds])
    return len(number_shots)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        n_, *birds_ = reader.read().rstrip().split('\n')
    print(shots(birds_))

    assert shots(['1 1', '2 2', '3 3', '2 1', '3 2', '3 1']) == 3
    assert shots(['1 1', '2 2', '3 3', '2 1', '3 2', '3 4']) == 3
