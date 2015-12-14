# --- Day 14: Reindeer Olympics ---
#
# This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their
# energy. Santa would like to know which of his reindeer is fastest, and so he has them race.
#
# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend
# whole seconds in either state.
#
# For example, suppose you have the following Reindeer:
#
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
#
# After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while
# Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on
# for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th
# second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.
#
# In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor
# Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000
# seconds).
#
# Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the
# winning reindeer traveled?
#
# --- Part Two ---
#
# Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.
#
# Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple
# reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as
# doing otherwise would be entirely ridiculous.
#
# Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in
# the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets
# his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139
# points by the 140th second.
#
# After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So,
# with the new scoring system, Dancer would win (if the race ended at 1000 seconds).
#
# Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points
# does the winning reindeer have?
data = open("day14_input").read().split("\n")

reindeer_stats = []

for d in data:
    stats = d.replace(" can fly ", " ") \
             .replace(" km/s for ", " ") \
             .replace(" seconds, but then must rest for ", " ") \
             .replace(" seconds.", "") \
             .split(" ")
    reindeer_stats.append(stats)

names = []
speed = {}
sprint_duration = {}
rest = {}
time_limit = 2503
greatest_distance = 0
winner = ""

for r in reindeer_stats:
    names.append(r[0])
    speed[r[0]] = int(r[1])
    sprint_duration[r[0]] = int(r[2])
    rest[r[0]] = int(r[3])

for name in names:
    distance = 0
    time_elapsed = 0

    while time_elapsed + sprint_duration[name] + rest[name] < time_limit:
        distance += speed[name] * sprint_duration[name]
        time_elapsed += sprint_duration[name] + rest[name]

    time_remaining = time_limit - time_elapsed
    if time_remaining > sprint_duration[name]:
        # There's still time for a full sprint
        distance += speed[name] * sprint_duration[name]
    else:
        # There's only time for part of the spring
        distance += speed[name] * time_remaining

    if distance > greatest_distance:
        greatest_distance = distance
        winner = name

print("{0} wins with a distance of {1}km".format(winner, greatest_distance))

# Part 2
distances = {name: 0 for name in names}
points = {name: 0 for name in names}

for time_elapsed in range(1, time_limit):
    # Move reindeer
    for name in names:
        if 0 < time_elapsed % (sprint_duration[name] + rest[name]) <= sprint_duration[name]:
            distances[name] += speed[name]

    # Award points
    highest = max(distances.values())

    for key, value in distances.items():
        if value == highest:
            points[key] += 1

winner = max(points, key=points.get)
print("{0} wins with {1} points".format(winner, points[winner]))
