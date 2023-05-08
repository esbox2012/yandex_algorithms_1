def cubes(ann_cubes: list, boris_cubes: list) -> tuple:
    ann_cubes, boris_cubes = set(ann_cubes), set(boris_cubes)
    common_cubes = [cube for cube in ann_cubes if cube in boris_cubes]
    ann_remaining_cubes = [cube for cube in ann_cubes if cube not in boris_cubes]
    boris_remaining_cubes = [cube for cube in boris_cubes if cube not in ann_cubes]
    return len(common_cubes), sorted(common_cubes), len(ann_remaining_cubes), sorted(ann_remaining_cubes), len(
        boris_remaining_cubes), sorted(boris_remaining_cubes)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        f = reader.read().rstrip().split('\n')

    n, m = list(map(int, f[0].split()))
    ann_cubes_ = list(map(int, f[1:n + 1]))
    boris_cubes_ = list(map(int, f[n + 1:]))

    for i in cubes(ann_cubes_, boris_cubes_):
        print(*i) if type(i) == list else print(i)

    assert cubes([1, 2], [2, 3]) == (1, [2], 1, [1], 1, [3])
    assert cubes([], []) == (0, [], 0, [], 0, [])
