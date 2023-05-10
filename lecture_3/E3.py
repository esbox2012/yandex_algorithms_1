def find_missing_buttons(xyz: list, n: str) -> int:
    using_buttons = set(int(button) for button in n)
    return len([button for button in using_buttons if button not in xyz])


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        f = reader.read().rstrip().split('\n')
    xyz_, n_ = list(map(int, f[0].split())), f[1]
    print(find_missing_buttons(xyz_, n_))

assert find_missing_buttons([1, 2, 3], '1001') == 1
assert find_missing_buttons([5, 7, 3], '123') == 2
