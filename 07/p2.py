def main():
    with open("input.txt") as f:
        cards = "J23456789TQKA"
        hands = [(0, 1, "null")]
        total = 0


        for l in f.readlines():
            hand, bid = l.split()

            # This time, iterate and find the best configuration
            meta_score = 0
            for card in cards:
                hand_with_jokers = hand.replace("J", card)
                hand_dict = { c: hand_with_jokers.count(c) for c in hand_with_jokers }

                match len(hand_dict):
                    # All five
                    case 1:
                        current_meta = 6
                    # All four / Full house
                    case 2:
                        if 4 in hand_dict.values():
                            current_meta = 5
                        else:
                            current_meta = 4
                    # All three / Two pairs
                    case 3:
                        if 3 in hand_dict.values():
                            current_meta = 3
                        else:
                            current_meta = 2
                    # One pair
                    case 4:
                        current_meta = 1
                    # All different
                    case 5:
                        current_meta = 0

                meta_score = max(meta_score, current_meta)

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
