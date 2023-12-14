def strdiff(s1, s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
    return diff


def find_reflection(board):
    imax = len(board)

    for i in range(imax-1):
        if 0 <= strdiff(board[i], board[i+1]) <= 1:
            diff = 0
            j = 0

            while i-j >= 0 and i+j+1 < imax and diff + strdiff(board[i-j], board[i+j+1]) <= 1:
                diff = diff + strdiff(board[i-j], board[i+j+1])
                j += 1

            while i-j >= 0 and i+j+1 < imax and board[i-j] == board[i+j+1]:
                j += 1

            if diff == 1 and (i-j < 0 or i+j+1 == imax):
                return i + 1
    return -1


def find_mirrors(board):
    v = find_reflection(board)
    if v != -1:
        return 100 * v

    board = [
        "".join([
            board[j][i]
            for j in range(len(board))
        ])
        for i in range(len(board[0]))
    ]

    return find_reflection(board)


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        total = 0

        board = []
        for line in lines:
            if line.strip():
                board.append(line.strip())
            else:
                total += find_mirrors(board)
                board = []

        print(total)


if __name__ == "__main__":
    main()
