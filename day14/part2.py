recipe_num = open("day14.input", "r").read().rstrip()

recipes = [3, 7]
ptr1, ptr2 = 0, 1

def add_recipes():
    sum_s = str(recipes[ptr1]+recipes[ptr2])
    for ch in sum_s:
        recipes.append(int(ch))

while True:
    add_recipes()
    ptr1 = (ptr1 + recipes[ptr1] + 1) % len(recipes)
    ptr2 = (ptr2 + recipes[ptr2] + 1) % len(recipes)
    last_chars = ''.join([str(e) for e in recipes[-20:]])
    if recipe_num in last_chars:
        print(''.join([str(e) for e in recipes]).index(recipe_num))
        break
