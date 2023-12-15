def hash(s):
    n = 0
    for c in s:
        n = ((n + ord(c)) * 17) % 256
    return n


def main():
    with open("input.txt") as f:
        total = 0
        hashmap = dict()

        for s in f.readline().split(","):
            # Case: =
            if "=" in s:
                label, value = s.split("=")
                box = hashmap.setdefault(hash(label), dict())
                box[label] = value
            # Case: -
            else:
                label, _ = s.split("-")
                box = hashmap.setdefault(hash(label), dict())
                box.pop(label, None)

        for box_index, box in hashmap.items():
            for slot_index, content in enumerate(box.items()):
                label, lens = content
                total += (box_index + 1) * (slot_index + 1) * int(lens)

        print(total)


if __name__ == "__main__":
    main()
