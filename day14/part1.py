recipe_num = int(open("day14.input", "r").read().rstrip())

recipes = [3, 7]
ptr1, ptr2 = 0, 1

def add_recipes():
    sum_s = str(recipes[ptr1]+recipes[ptr2])
    for ch in sum_s:
        recipes.append(int(ch))

while len(recipes) < recipe_num + 10:
    add_recipes()
    ptr1 = (ptr1 + recipes[ptr1] + 1) % len(recipes)
    ptr2 = (ptr2 + recipes[ptr2] + 1) % len(recipes)

print(''.join([str(r) for r in recipes[recipe_num:recipe_num+10]]))
