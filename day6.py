# --- Day 6: Probably a Fire Hazard ---
#
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to
# deploy one million lights in a 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the
# ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at
# 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive
# ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a
# coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent
# you in order.
#
# For example:
#
# - turn on 0,0 through 999,999 would turn on (or leave on) every light.
# - toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning
# on the ones that were off.
# - turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
#
# After following the instructions, how many lights are lit?
#
#
# --- Part Two ---
#
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from
# Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or
# more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's instructions?
#
# For example:
#
# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

instructions = open("day6_input").read().split("\n")

grid_part1 = [[0 for x in range(1000)] for x in range(1000)]
grid_part2 = [[0 for x in range(1000)] for x in range(1000)]

for instruction in instructions:
    coords = list(map(int, ''.join(i for i in instruction if not i.isalpha()).strip().replace(",", "  ").split("  ")))
    operation = "toggle" if instruction.startswith("toggle") else "on" if instruction.startswith("turn on") else "off"

    for x in range(coords[0], coords[2] + 1):
        for y in range(coords[1], coords[3] + 1):
            if operation == "toggle":
                grid_part1[x][y] = 1 if grid_part1[x][y] == 0 else 0
                grid_part2[x][y] += 2
            elif operation == "on":
                grid_part1[x][y] = 1
                grid_part2[x][y] += 1
            elif operation == "off":
                grid_part1[x][y] = 0
                grid_part2[x][y] = 0 if grid_part2[x][y] == 0 else grid_part2[x][y] - 1

print("Lights on = {0}".format(sum(sum(i) for i in grid_part1)))
print("Total brightness = {0}".format(sum(sum(i) for i in grid_part2)))
