def minesweeper(mines: list, columns: int, rows: int) -> list:
    mat = [[0] * columns for _ in range(rows)]
    for mine in mines:
        x, y = (int(i) - 1 for i in mine.split())
        mat[x][y] = '*'
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [0, -1], [-1, -1], [-1, 0], [1, -1]]
        for direction in directions:
            newx, newy = x + direction[0], y + direction[1]
            if 0 <= newx < rows and 0 <= newy < columns and mat[newx][newy] != '*':
                mat[newx][newy] += 1
    return mat


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        f = reader.read().rstrip().split('\n')
    n_rows, m_columns, k_mines = list(map(int, f[0].split()))

    result = minesweeper(f[1:], m_columns, n_rows)
    for i in result:
        print(*i)

    assert minesweeper([], 2, 2) == [[0, 0], [0, 0]]
    assert minesweeper(['1 3', '2 1', '4 2', '4 4'], 4, 4) == [[1, 2, '*', 1], ['*', 2, 1, 1], [2, 2, 2, 1],
                                                               [1, '*', 2, '*']]
