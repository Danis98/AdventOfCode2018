import string

polymer = open("day5.input", "r").read().rstrip()

stack = []

def reacts(a, b):
    return a.lower() == b.lower() and a != b

for monomer in polymer:
    if len(stack) == 0 or not reacts(monomer, stack[-1]):
        stack += monomer
    elif reacts(monomer, stack[-1]):
        stack = stack[:-1]
print(len(stack))
