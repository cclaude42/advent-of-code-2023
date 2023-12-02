import re

total = 0
nstrings = ["zero","one","two","three","four","five","six","seven","eight","nine"]

with open("input.txt") as f:
    for l in f.readlines():
        nums = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l)
        nums = [nstrings.index(num) if num in nstrings else int(num) for num in nums]
        total += nums[0] * 10 + nums[-1]

print(total)