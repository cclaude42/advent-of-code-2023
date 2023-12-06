def fragment_outcomes(distance, alltime, time_start, time_end, desired_outcome):
    first_yes, last_no = -1, -1
    timediff = time_end - time_start
    timesplit = timediff // 100
    if timesplit == 0:
        timesplit = 1


    for n in range(time_start, time_end, timesplit):
        outcome = n * (alltime - n) > distance
        if outcome == desired_outcome:
            first_yes = n
            break
        else:
            last_no = n

    if first_yes == -1:
        first_yes = time_end


    if first_yes - last_no == 1:
        return first_yes
    else:
        return fragment_outcomes(distance, alltime, last_no, first_yes, desired_outcome)


def main():
    with open("input.txt") as f:
        time, distance = [int("".join(s.split(":")[1].split())) for s in f.readlines()]

        start = fragment_outcomes(distance, time, 0, time, True)
        end = fragment_outcomes(distance, time, start, time, False)

        print(end - start)


if __name__ == "__main__":
    main()
