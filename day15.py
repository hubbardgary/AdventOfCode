# --- Day 15: Science for Hungry People ---
#
# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right
# balance of ingredients.
#
# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you
# could use to finish the recipe (your puzzle input) and their properties per teaspoon:
#
# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
#
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can
# reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties
# (negative totals become 0) and then multiplying together everything except calories.
#
# For instance, suppose you have these two ingredients:
#
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
#
# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each
# ingredient must add up to 100) would result in a cookie with the following properties:
#
# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
#
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880,
# which happens to be the best score possible given these ingredients. If any properties had produced a negative total,
# it would have instead become zero, causing the whole score to multiply to zero.
#
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you
# can make?
#
# -- Part 2 --
# Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories
# per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100
# teaspoons, same ingredients, same scoring system).
#
# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of
# cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go
# down, though: only 57600000, the best you can do in such trying circumstances.
#
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you
# can make with a calorie total of 500?
data = open("day15_input").read().split("\n")
parsed_data = []

for d in data:
    if len(d) > 0:
        props = d.replace(": capacity ", " ") \
                 .replace(", durability ", " ") \
                 .replace(", flavor ", " ") \
                 .replace(", texture ", " ") \
                 .replace(", calories ", " ") \
                 .split(" ")
        parsed_data.append(props)

capacities = []
durabilities = []
flavors = []
textures = []
calories = []

for d in parsed_data:
    capacities.append(int(d[1]))
    durabilities.append(int(d[2]))
    flavors.append(int(d[3]))
    textures.append(int(d[4]))
    calories.append(int(d[5]))

high_score = 0
high_score_500_cals = 0

for i in range(1, 98):
    for j in range(1, 98):
        if i + j > 100:
            continue
        for k in range(1, 98):
            l = 100 - i - j - k
            if l > 0:  # i.e. i, j, k and l sum to 100
                capacity = capacities[0] * i + capacities[1] * j + capacities[2] * k + capacities[3] * l
                durability = durabilities[0] * i + durabilities[1] * j + durabilities[2] * k + durabilities[3] * l
                flavor = flavors[0] * i + flavors[1] * j + flavors[2] * k + flavors[3] * l
                texture = textures[0] * i + textures[1] * j + textures[2] * k + textures[3] * l
                total_calories = calories[0] * i + calories[1] * j + calories[2] * k + calories[3] * l
                if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                    score = 0
                else:
                    score = capacity * durability * flavor * texture
                if score > high_score:
                    high_score = score
                if total_calories == 500 and score > high_score_500_cals:
                    high_score_500_cals = score

print("Highest scoring cookie = {0}".format(high_score))
print("Highest scoring cookie of 500 calories = {0}".format(high_score_500_cals))
