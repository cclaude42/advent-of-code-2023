def compute_game (game, gameid):
    mincubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for gameround in game.split("; "):
        for cubeset in gameround.split(", "):
            n, color = cubeset.split(" ")

            if (int(n) > mincubes[color]):
                mincubes[color] = int(n)

    return mincubes["red"] * mincubes["green"] * mincubes["blue"]
    

total = 0
maxcubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt") as f:
    for l in f.readlines():
        head, game = l.split(": ")
        _, gameid = head.split(" ")

        total += compute_game(game, gameid)

print(total)
