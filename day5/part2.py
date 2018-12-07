import string

polymer = open("day5.input", "r").read().rstrip()

def reacts(a, b):
    return a.lower() == b.lower() and a != b

def react(removed):
    global polymer
    stack = []
    for monomer in polymer:
        if monomer in removed:
            continue
        elif len(stack) == 0 or not reacts(monomer, stack[-1]):
            stack += monomer
        elif reacts(monomer, stack[-1]):
            stack = stack[:-1]
    return len(stack)

min_len = react([])
for letter in string.ascii_lowercase:
    min_len = min(min_len, react([letter, letter.upper()]))
print min_len
