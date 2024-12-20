from functools import cache
 
with open("data1.txt") as f:
    towels, patterns = f.read().split("\n\n")
 
towels = towels.split(", ")
patterns = patterns.splitlines()
 
@cache
def count_possibilities(remaining_pattern):
    if remaining_pattern == "":
        return 1
    else:
        possibilities = 0
        for towel in towels:
            if remaining_pattern.startswith(towel):
                possibilities += count_possibilities(remaining_pattern[len(towel):])
        return possibilities
 
possibilities = [count_possibilities(p) for p in patterns]
 
# 1
print(sum([p > 0 for p in possibilities]))
 
# 2
print(sum(possibilities))
