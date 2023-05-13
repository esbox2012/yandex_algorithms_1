def count_honest_turtles(turtles: list, amount_of_turtles: int) -> int:
    if not isinstance(amount_of_turtles, int):
        raise TypeError('Use numbers')
    honest_turtles = set()
    for turtle in turtles:
        a_front, b_back = map(int, turtle.split())
        if a_front >= 0 and b_back >= 0 and a_front + b_back == amount_of_turtles - 1:
            honest_turtles.add(a_front)
    return len(honest_turtles)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        amount_of_turles, *turtles = reader.read().rstrip().split('\n')
    amount_of_turles = int(amount_of_turles)
    print(count_honest_turtles(turtles, amount_of_turles))

    assert count_honest_turtles(['0 4', '1 3', '2 2', '3 1', '4 0'], 5) == 5
    assert count_honest_turtles(['9 1', '8 1', '7 2', '6 2', '5 3', '4 4', '3 6', '2 7', '1 9', '0 8'], 10) == 4
