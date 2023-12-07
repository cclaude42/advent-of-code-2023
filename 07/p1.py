def main():
    with open("input.txt") as f:
        cards = "23456789TJQKA"
        hands = [(0, 1, "null")]
        total = 0


        for l in f.readlines():
            hand, bid = l.split()

            # Start by assigning a meta-score to a hand by computing its duplicates
            hand_dict = { c: hand.count(c) for c in hand }
            match len(hand_dict):
                # All five
                case 1:
                    meta_score = 6
                # All four / Full house
                case 2:
                    if 4 in hand_dict.values():
                        meta_score = 5
                    else:
                        meta_score = 4
                # All three / Two pairs
                case 3:
                    if 3 in hand_dict.values():
                        meta_score = 3
                    else:
                        meta_score = 2
                # One pair
                case 4:
                    meta_score = 1
                # All different
                case 5:
                    meta_score = 0

            # Then iterate through cards, multiplying score and appending, like you would do in an atoi
            hand_nums = [cards.index(c) for c in hand]
            for card in hand_nums:
                meta_score = meta_score * 13 + card

            hands.append((meta_score, int(bid), hand))

        hands = sorted(hands, key=lambda x: x[0])
        for i, hand in enumerate(hands):        
            _, bid, _ = hand
            total += i * bid

        print(total)


if __name__ == "__main__":
    main()
