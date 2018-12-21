NUM = 10551403

div_sum = 0
for i in range(1, NUM+1):
    if NUM % i == 0:
        div_sum += i
print(div_sum)
