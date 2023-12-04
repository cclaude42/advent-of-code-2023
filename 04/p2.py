def main():
    with open("input.txt") as f:
        total = 0
        scratchcards = dict()

        # Read scratchcards to see how many cards they yield
        for l in f.readlines():
            head, game = l.split(":")
            card_id = int(head.split()[1])
            winning, scratched = (g.strip().split() for g in game.split("|"))

            scratchcards[card_id] = len([n for n in scratched if n in winning])

        # Refactor dict to reflect cards given
        card_max = max(scratchcards.keys())
        for card_id, ncards in scratchcards.items():
            scratchcards[card_id] = list(range(card_id + 1, min(card_id + ncards, card_max) + 1))

        # Simulate until no more cards
        cards = list(scratchcards.keys())
        while cards:
            card = cards.pop()
            cards += scratchcards[card]
            total += 1

        print(total)


if __name__ == "__main__":
    main()
