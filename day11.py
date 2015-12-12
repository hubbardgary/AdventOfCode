# --- Day 11: Corporate Policy ---
#
# Santa's previous password expired, and he needs help choosing a new one.
#
# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a
# password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters
# (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is
# valid.
#
# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one
# step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.
#
# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password
# requirements:
#
# - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
# They cannot skip letters; abd doesn't count.
# - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
# therefore confusing.
# - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

# For example:
# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement
# (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi...,
# since i is not allowed.

# Given Santa's current password (vzbxkghb), what should his next password be?
#
# --- Part Two ---
#
# Santa's password expired again. What's the next one?


def increment_password(ascii_codes):
    for i in range(len(ascii_codes) - 1, -1, -1):
        if ascii_codes[i] < 122:
            ascii_codes[i] += 1
            break
        ascii_codes[i] = 97
    return ascii_codes


def contains_permitted_chars(ascii_list):
    for ch in ["i", "o", "l"]:
        if ord(ch) in ascii_list:
            return False
    return True


def contains_3_increasing_chars(ascii_list):
    for i in range(len(ascii_list) - 2):
        if ascii_list[i] == ascii_list[i+1] - 1 == ascii_list[i+2] - 2:
            return True
            break
    return False


def contains_2_non_repeating_pairs(ascii_list):
    i = 0
    pairs_count = 0
    while i < len(ascii_list) - 1:
        if ascii_list[i] == ascii_list[i+1]:
            pairs_count += 1
            if pairs_count == 2:
                return True
            i += 2  # ensure non-overlapping
            continue
        i += 1
    return False


def conforms_to_rules(ascii_list):
    return contains_permitted_chars(ascii_list) and \
           contains_3_increasing_chars(ascii_list) and \
           contains_2_non_repeating_pairs(ascii_list)

password = "vzbxkghb"

ascii_pw_chars = []

for x in range(len(password)):
    ascii_pw_chars.append(ord(password[x]))

passwords_found = 0
while passwords_found < 2:
    next_password = increment_password(ascii_pw_chars)
    if conforms_to_rules(next_password):
        print("".join(map(chr, ascii_pw_chars)))
        passwords_found += 1
