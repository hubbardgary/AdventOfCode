# --- Day 9: All in a Single Night ---
#
# Every year, Santa manages to deliver all of his presents in a single night.
#
# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair
# of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly
# once. What is the shortest distance he can travel to achieve this?
#
# For example, given the following distances:
#
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:
#
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
#
# What is the distance of the shortest route?
#
#
# --- Part Two ---
#
# The next year, just to show off, Santa decides to take the route with the longest distance instead.
#
# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly
# once.
#
# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
#
# What is the distance of the longest route?

import itertools

distances = open("day9_input").read().split("\n")
vertices = {}

# Build dictionary of dictionaries mapping distance between each location
for distance in distances:
    d = distance.replace(" to ", " ").replace(" = ", " ").split(" ")
    if len(d) == 3:
        if d[0] not in vertices:
            vertices[d[0]] = {}
        if d[1] not in vertices:
            vertices[d[1]] = {}
        vertices[d[0]][d[1]] = int(d[2])
        vertices[d[1]][d[0]] = int(d[2])

# This is the Hamiltonian Path problem, which is NP-complete.
# So for once I can brute force it without feeling guilty.
shortest_path = float("inf")
longest_path = 0
possible_routes = list(itertools.permutations(list(vertices.keys())))

for route in possible_routes:
    route_len = 0
    current_loc = ""
    next_loc = ""
    for loc in route:
        if current_loc == "":
            current_loc = loc
            continue
        next_loc = loc
        route_len += vertices[current_loc][next_loc]
        current_loc = next_loc
    if route_len < shortest_path:
        shortest_path = route_len
    if route_len > longest_path:
        longest_path = route_len

print("Shortest path: {0}".format(shortest_path))
print("Longest path: {0}".format(longest_path))
