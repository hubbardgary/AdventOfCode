# --- Day 5: Doesn't He Have Intern-Elves For This? ---
#
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of
# the disallowed substrings. aaa is nice because it has at least three vowels and a double letter, even though the
# letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
# How many strings are nice?


# --- Part Two ---
#
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or
# nice. None of the old rules apply, as they are all clearly ridiculous.
#
# Now, a nice string is one with all of the following properties:
#
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy)
# or aabcdefgaa (aa), but not like aaa (aa, but it overlaps). It contains at least one letter which repeats with
# exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:
#
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one
# letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the
# letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
#
# How many strings are nice under these new rules?
#
#
# Fantastic regex resource: https://regex101.com/

import re


def nice_string_part1(string):
    if len(re.findall("[aeiou]", string)) > 2 and \
            not re.search("(ab|cd|pq|xy)", string) and \
            re.search(r"(.)\1", string):
        return True
    return False


def nice_string_part2(string):
    if re.search(r'(..).*\1', string) and re.search(r'(.).\1', string):
        return True
    return False


data = open("day5_input").read()
nice_count_1 = 0
nice_count_2 = 0

strings = data.split("\n")
for s in strings:
    if nice_string_part1(s):
        nice_count_1 += 1
    if nice_string_part2(s):
        nice_count_2 += 1

print("Part 1 = {0}".format(nice_count_1))
print("Part 2 = {0}".format(nice_count_2))
