# --- Day 18: Like a GIF For Your Yard ---
#
# After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed.
# You arrange them in a 100x100 grid.
#
# Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few
# lights, he says, you'll have to resort to animation.
#
# Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means
# "off".
#
# Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each
# light's next state (either on or off) depends on its current state and the current states of the eight lights
# adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the
# missing ones always count as "off".
#
# For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light
# marked B, which is on an edge, only has the neighbors marked 1 through 5:
#
# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.
#
# The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:
#
# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
# All of the lights update simultaneously; they all consider the same current state before moving to the next.
#
# Here's a few steps from an example configuration of another 6x6 grid:
#
# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
#
# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..
#
# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
#
# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
#
# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
#
#  After 4 steps, this example has four lights on.
#
# In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
#
# --- Part Two ---
#
# You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game
# of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights,
# one in each corner, are stuck on and can't be turned off. The example above will actually run like this:
#
# Initial state:
# ##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#
#
# After 1 step:
# #.##.#
# ####.#
# ...##.
# ......
# #...#.
# #.####
#
# After 2 steps:
# #..#.#
# #....#
# .#.##.
# ...##.
# .#..##
# ##.###
#
# After 3 steps:
# #...##
# ####.#
# ..##.#
# ......
# ##....
# ####.#
#
# After 4 steps:
# #.####
# #....#
# ...#..
# .##...
# #.....
# #.#..#
#
# After 5 steps:
# ##.###
# .##..#
# .##...
# .##...
# #.#...
# ##...#
# After 5 steps, this example now has 17 lights on.
#
# In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state,
# how many lights are on after 100 steps?


def get_initial_layout(filename):
    file = open(filename)
    lights = []
    for line in file:
        row = []
        for c in line:
            if c is not "\n":
                row.append(c)
        lights.append(row)
    return lights


def switch_on_corner_lights(grid):
    grid[0][0] = "#"
    grid[0][99] = "#"
    grid[99][0] = "#"
    grid[99][99] = "#"
    return grid


def in_bounds(grid, x, y):
    return -1 < x < len(grid) and -1 < y < len(grid[0])


def neighbours_lit(grid, x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if in_bounds(grid, i, j) and not(i == x and j == y):
                if grid[i][j] == "#":
                    count += 1
    return count


def next_matrix(current_matrix, broken_lights):
    new_matrix = [[0 for x in range(100)] for x in range(100)]
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix)):
            if current_matrix[i][j] == "#":
                if 1 < neighbours_lit(current_matrix, i, j) < 4:   # on and 2 or 3 neighbours lit
                    new_matrix[i][j] = "#"
                else:
                    new_matrix[i][j] = "."
            else:
                if neighbours_lit(current_matrix, i, j) == 3:   # off and 3 neighbours lit
                    new_matrix[i][j] = "#"
                else:
                    new_matrix[i][j] = "."
    if broken_lights:
        return switch_on_corner_lights(new_matrix)
    return new_matrix


def print_grid(grid):
    for i in range(len(grid)):
        print("".join(grid[i]))

# Part 1
matrix = get_initial_layout("day18_input")
for x in range(100):
    old_matrix = list(matrix)
    matrix = next_matrix(old_matrix, False)
print("Part 1 = {0}".format(sum(x.count("#") for x in matrix)))

# Part 2
matrix = switch_on_corner_lights(get_initial_layout("day18_input"))
for x in range(100):
    old_matrix = list(matrix)
    matrix = next_matrix(old_matrix, True)
print("Part 2 = {0}".format(sum(x.count("#") for x in matrix)))
