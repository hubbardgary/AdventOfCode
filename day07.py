# --- Day 7: Some Assembly Required ---
#
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is
# a little under the recommended age range, and he needs help assembling the circuit.
#
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A
# signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal
# from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its
# inputs have a signal.
#
# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires
# x and y to an AND gate, and then connect its output to wire z.
#
# For example:
#
# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate
# the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for
# these gates.
#
# For example, here is a simple circuit:
#
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:
#
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided
# to wire a?
#
#
# --- Part Two ---
#
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
# What new signal is ultimately provided to wire a?

def apply_op(op_code, *operands):
    for o in operands:
        if o is None:
            return
    if op_code == "LSHIFT":
        return operands[0] << operands[1]
    elif op_code == "RSHIFT":
        return operands[0] >> operands[1]
    elif op_code == "AND":
        return operands[0] & operands[1]
    elif op_code == "OR":
        return operands[0] | operands[1]
    elif op_code == "NOT":
        return ~ operands[0] & 0xffff  # ensure 16 bit result


def do_operation(instr):
    if len(instr) == 1:
        return get_value(instr[0])
    elif len(instr) == 2:
        return apply_op(instr[0], get_value(instr[1]))
    else:
        return apply_op(instr[1], get_value(instr[0]), get_value(instr[2]))


def get_value(v):
    if not v.isalpha():
        return int(v)
    if v in register:
        return int(register[v])


def run_instructions():
    for i in instructions:
        i = i.split(" -> ")
        operation = i[0]
        address = i[1]

        result = do_operation(operation.split(" "))
        if result is not None:
            register[address] = result


instructions = open("day07_input").read().split("\n")
register = dict()

while "a" not in register:
    run_instructions()
    
part1_answer = register["a"]  # Part 1 solution found

# Part 2
register = dict()
register["b"] = part1_answer

for s in instructions:
    if s.endswith("-> b"):
        instructions.remove(s)

while "a" not in register:
    run_instructions()

part2_answer = register["a"]

print("Part 1: a = {0}".format(part1_answer))
print("Part 2: a = {0}".format(part2_answer))
