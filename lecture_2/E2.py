def Find_Vasya(results: list, num: int) -> list:
    champ = max(results)
    keychamp = results.index(champ)
    vasya = []
    for i in range(1, num - 1):
        if results[i] > results[i + 1] and str(results[i])[-1] == '5' and i > keychamp:
            vasya.append(results[i])
    return vasya


def Place_Vasya(results: list, keys: list, num: int) -> int:
    if not keys: return 0
    key = max(keys)
    count = 1
    for i in range(num):
        if results[i] > key: count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        f = reader.read().rstrip().split('\n')
    num_ = int(f[0])
    results_ = list(map(int, f[1].split()))

    print(Place_Vasya(results_, Find_Vasya(results_, num_), num_))

    assert Find_Vasya([10, 20, 15, 10, 30, 5, 1], 7) == [5]
    assert Find_Vasya([15, 15, 10], 3) == [15]
    assert Find_Vasya([10, 15, 20], 3) == []

    assert Place_Vasya([10, 20, 15, 10, 30, 5, 1], [5], 7) == 6
    assert Place_Vasya([15, 15, 10], [15], 3) == 1
    assert Place_Vasya([10, 15, 20], [], 3) == 0
