import re

total = 0

with open("input.txt") as f:
    for l in f.readlines():
        nums = re.findall("\d", l)
        total += int(nums[0] + nums[-1])

print(total)