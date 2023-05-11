def make_pairs(sequence: str) -> list:
    return [sequence[i:i + 2] for i in range(len(sequence) - 1)]


def make_genome_dict(genome: list) -> dict:
    genome_dict = dict()
    for pair in genome:
        genome_dict[pair] = genome_dict.get(pair, 0) + 1
    return genome_dict


def similarity(genome_1: str, genome_2: str) -> int:
    count = 0
    genome_1 = make_pairs(genome_1)
    genome_2 = set(make_pairs(genome_2))
    genome_1_dict = make_genome_dict(genome_1)
    for pair in genome_2:
        if pair in genome_1_dict:
            count += genome_1_dict[pair]
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        genome_1_, genome_2_ = reader.read().rstrip().split('\n')

    print(similarity(genome_1_, genome_2_))

    assert similarity('ABCDE', 'ABC') == 2
    assert similarity('ABABAB', 'ABC') == 3
    assert similarity('ABABAB', 'ABA') == 5
