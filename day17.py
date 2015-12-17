# --- Day 17: No Such Thing as Too Much ---
#
# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to
# move it into smaller containers. You take an inventory of the capacities of the available containers.
#
# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there
# are four ways to do it:
#
# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
#
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of
# eggnog?
#
# --- Part Two ---
#
# While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving
# department is requesting as many containers as you can spare.
#
# Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you
# fill that number of containers and still hold exactly 150 litres?
#
# In the example above, the minimum number of containers was two. There were three ways to use that many containers,
# and so the answer there would be 3.
import itertools

containers = list(map(int, open("day17_input").read().split("\n")))

combinations = 0
min_length = 999
min_count = 0

for i in range(0, len(containers)+1):
    for subset in itertools.combinations(containers, i):
        if sum(subset) == 150:
            combinations += 1
            if len(subset) < min_length:
                min_length = len(subset)
                min_count = 0
            if len(subset) == min_length:
                min_count += 1

print("Part 1: {0}".format(combinations))
print("Part 2: {0}".format(min_count))
