REG_NUM = 6

regs = [0 for i in range(REG_NUM)]
ip_reg = -1

code = open("day19.input", "r").read().rstrip().split("\n")

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

def exec_instruction(instr, regs, ip_reg, a, b, c):
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
        exit(0)
    regs[ip_reg] += 1

if code[0][0] == '#':
    ip_reg = int(code[0].split(" ")[1])
    code.pop(0)

while regs[ip_reg] in range(len(code)):
    line = code[regs[ip_reg]]
    instr = line.split(" ")[0]
    a, b, c = [int(e) for e in line.split(" ")[1:]]
    exec_instruction(instr, regs, ip_reg, a, b, c)

print(regs[0])
