# --- Day 4: The Ideal Stocking Stuffer ---
#
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically
# forward-thinking little girls and boys.
#
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the
# MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins,
# you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
# For example:
#
# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes
# (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is
# 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
#
# Your puzzle input is iwrupvqb.
#
# --- Part Two ---
#
# Now find one that starts with six zeroes.

import hashlib

md5 = ""
i = 0
part_1_found = False

while not md5.startswith("000000"):
    i += 1
    m = hashlib.md5()
    m.update(b"iwrupvqb%d" % i)
    md5 = m.hexdigest()

    if md5.startswith("00000") and not part_1_found:
        # Print Part 1 answer
        print("MD5 = {0}, created using {1}".format(md5, i))
        part_1_found = True

# Print Part 2 answer
print("MD5 = {0}, created using {1}".format(md5, i))
