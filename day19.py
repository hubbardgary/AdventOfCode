# --- Day 19: Medicine for Rudolph ---
#
# Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.
#
# Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine.
# Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.
#
# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any
# Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of
# replacements, one per step, until it has the right molecule.
#
# However, the machine has to be calibrated before it can be used. Calibration involves determining the number of
# molecules that can be generated in one step from a given starting point.
#
# For example, imagine a simpler machine that supports only the following replacements:
#
# H => HO
# H => OH
# O => HH
# Given the replacements above and starting with HOH, the following molecules could be generated:
#
# HOOH (via H => HO on the first H).
# HOHO (via H => HO on the second H).
# OHOH (via H => OH on the first H).
# HOOH (via H => OH on the second H).
# HHHH (via O => HH).
#
# So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement
# from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and
# three from O).
#
# The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition
# H => OO would result in OO2O.
#
# Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you
# need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one
# replacement on the medicine molecule?
#
# --- Part Two ---
#
# Now that the machine is calibrated, you're ready to begin molecule fabrication.
#
# Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like
# the ones during calibration.
#
# For example, suppose you have the following replacements:
#
# e => H
# e => O
# H => HO
# H => OH
# O => HH
#
# If you'd like to make HOH, you start with e, and then make the following replacements:
#
# e => O to get O
# O => HH to get HH
# H => OH (on the second H) to get HOH
#
# So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.
#
# How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle
# input, what is the fewest number of steps to go from e to the medicine molecule?
import random

data = open("day19_input").read().split("\n")

medicine_molecule = ""

conversions = []
for line in data:
    if " => " in line:
        l = line.split(" => ")
        conversions.append([l[0], l[1]])
    elif len(line) > 0:
        medicine_molecule = line

distinct_molecules = []
for i in range(0, len(medicine_molecule)):
    for c in conversions:
        if medicine_molecule[i:].startswith(c[0]):
            new_molecule = medicine_molecule[0:i] + medicine_molecule[i:].replace(c[0], c[1], 1)
            if new_molecule not in distinct_molecules:
                distinct_molecules.append(new_molecule)

print("Part 1 = {0}".format(len(distinct_molecules)))

# Part 2
molecule = medicine_molecule
count = 0
change_made = True

while molecule != "e":
    # Try applying conversions in random order.
    # Reaching "e" always takes the same amount of steps, and applying a random order
    # seems to be more efficient in this case than attacking it methodically
    random.shuffle(conversions)
    change_made = False
    for x in conversions:
        if x[1] in molecule:
            molecule = molecule.replace(x[1], x[0], 1)
            count += 1
            change_made = True
            random.shuffle(conversions)  # shuffling again is much quicker but need to rethink the structure of for loop
    if not change_made and molecule != "e":
        # We've hit a dead end and haven't found "e", so reset and try again
        molecule = medicine_molecule
        count = 0

print("Part 2 = {0}".format(count))
