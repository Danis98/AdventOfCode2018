input_raw = open("day16.input", "r").read().rstrip()

samples = input_raw.split("\n\n\n")[0].split("\n\n")

candidates = {}

instructions = [
    "addr",
    "addi",
    "mulr",
    "muli",
    "banr",
    "bani",
    "borr",
    "bori",
    "setr",
    "seti",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr"
]

def exec_instruction(instr, regs, a, b, c):
    if instr == 'addr':
        v_a = regs[a]
        v_b = regs[b]
        regs[c] = v_a + v_b
    elif instr == 'addi':
        v_a = regs[a]
        v_b = b
        regs[c] = v_a + v_b
    elif instr == 'mulr':
        v_a = regs[a]
        v_b = regs[b]
        regs[c] = v_a * v_b
    elif instr == 'muli':
        v_a = regs[a]
        v_b = b
        regs[c] = v_a * v_b
    elif instr == 'banr':
        v_a = regs[a]
        v_b = regs[b]
        regs[c] = v_a & v_b
    elif instr == 'bani':
        v_a = regs[a]
        v_b = b
        regs[c] = v_a & v_b
    elif instr == 'borr':
        v_a = regs[a]
        v_b = regs[b]
        regs[c] = v_a | v_b
    elif instr == 'bori':
        v_a = regs[a]
        v_b = b
        regs[c] = v_a | v_b
    elif instr == 'setr':
        v_a = regs[a]
        regs[c] = v_a
    elif instr == 'seti':
        v_a = a
        regs[c] = v_a
    elif instr == 'gtir':
        v_a = a
        v_b = regs[b]
        regs[c] = 1 if v_a > v_b else 0
    elif instr == 'gtri':
        v_a = regs[a]
        v_b = b
        regs[c] = 1 if v_a > v_b else 0
    elif instr == 'gtrr':
        v_a = regs[a]
        v_b = regs[b]
        regs[c] = 1 if v_a > v_b else 0
    elif instr == 'eqir':
        v_a = a
        v_b = regs[b]
        regs[c] = 1 if v_a == v_b else 0
    elif instr == 'eqri':
        v_a = regs[a]
        v_b = b
        regs[c] = 1 if v_a == v_b else 0
    elif instr == 'eqrr':
        v_a = regs[a]
        v_b = regs[b]
        regs[c] = 1 if v_a == v_b else 0
    else:
        print("What is %s?" % instr)

def get_candidates(sample):
    lines = sample.split("\n")
    init_regs = [int(e) for e in lines[0].split(": ")[1][1:-1].split(", ")]
    final_regs = [int(e) for e in lines[2].split(":  ")[1][1:-1].split(", ")]
    instr_code, a, b, c = [int(e) for e in lines[1].split(" ")]

    sample_matches = set()
    for instr in instructions:
        regs = init_regs[:]
        exec_instruction(instr, regs, a, b, c)
        if regs == final_regs:
            sample_matches.add(instr)

    if instr_code not in candidates:
        candidates[instr_code] = sample_matches
    else:
        candidates[instr_code] = candidates[instr_code].intersection(sample_matches)

for sample in samples:
    get_candidates(sample)

instruction_codes = {}
assigned = set()
cont = True
while cont:
    cont = False
    for code in candidates:
        if len(candidates[code]) == 1:
            for elem in candidates[code]:
                break
            if elem not in assigned:
                assigned.add(elem)
                instruction_codes[code] = elem
                cont = True
                break
        else:
            to_remove = set()
            for cand in candidates[code]:
                if cand in assigned:
                    to_remove.add(cand)
            candidates[code] -= to_remove
            if len(candidates[code]) == 1:
                for elem in candidates[code]:
                    break
                if elem not in assigned:
                    assigned.add(elem)
                    instruction_codes[code] = elem
                    cont = True
                    break

program = input_raw.split("\n\n\n")[1].split("\n")[1:]

regs = [0, 0, 0, 0]
for line in program:
    instr_code, a, b, c = [int(e) for e in line.split(" ")]
    exec_instruction(instruction_codes[instr_code], regs, a, b, c)

print(regs[0])
