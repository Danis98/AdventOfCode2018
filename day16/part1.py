input_raw = open("day16.input", "r").read().rstrip()

samples = input_raw.split("\n\n\n")[0].split("\n\n")

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

    match_ctr = 0
    for instr in instructions:
        regs = init_regs[:]
        exec_instruction(instr, regs, a, b, c)
        if regs == final_regs:
            match_ctr += 1
    return match_ctr

res = 0
for sample in samples:
    if get_candidates(sample) >= 3:
        res += 1

print(res)
