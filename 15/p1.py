def hash(s):
    n = 0
    for c in s:
        n = ((n + ord(c)) * 17) % 256
    return n

def main():
    with open("input.txt") as f:
        total = 0

        for s in f.readline().split(","):
            total += hash(s)

        print(total)


if __name__ == "__main__":
    main()
