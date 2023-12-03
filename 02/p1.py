def compute_game (game, gameid):
    for gameround in game.split("; "):
        for cubeset in gameround.split(", "):
            n, color = cubeset.split(" ")

            if (int(n) > maxcubes[color]):
                return 0

    return int(gameid)
    

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
