#!/usr/bin/env python3
# Copyright 2018 Lulu Wang

import math
#6 inch cake ingredients
size_original = 6

ingredient_names = ['Cake_eggs', 'Cake_oil', 'Cake_sugar', 'Cake_matcha', 'Cake_salt', 'Cake_milk', 'Cake_flour',
     'Mousse_gelatine', 'Mousse_matcha', 'Mousse_milk', 'Mousse_sugar', 'Mousse_cream', 'Mousse_cheese']
ingredient_value = [3, 25, 60, 1, 1, 60, 60, 2, 1, 125, 70, 175, 100]
ingredient_unit = ['eggs', 'g', 'g', 'tbsp', 'pinch', 'g', 'g', 'slices', 'tbsp', 'g', 'g', 'g', 'g']

size_request = input('How big is the cake you want? ')  #Prompt

size = ('6','8','9','10','11','12')  # cake size optipn
count = 0
max_attempt = 3  # times can try 

def myround(n, d = 0): 
    a = n * (10 ** (d + 1))
    a = math.floor(a)
    a = a / 10
    b = math.floor(a)
    difference = a - b
    
    if ( difference < 0.5):
        result = b
    else:
        result = b + 1
        
    result = result / (10 ** d)
    
    if (d == 0) :
        result = int(result)
    
    return result

def print_part(part_name, filter):
    s = part_name
    for i in range(length):
        name = ingredient_names[i]
        if (name.startswith(filter)):
            continue

        value = new_value[i]
        s = s + f'{name}: {value} {ingredient_unit[i]}' + ', '
    
    print(s)

while (size_request not in size):
    count +=1
    if count > max_attempt: 
        print('You entered more than 3 times and you cannot try more')
        break
    size_request = input(f"Sorry, we don't have this cake size, could you change the cake size?({count} times) ")
else:
    size_now = size_request
    ingredient_multiple = int(size_now) ** 2 / size_original **2
    ingredient_multiple = float(ingredient_multiple)

    new_value = list()

    length = len(ingredient_value)

    for i in range(length):
        old_value = ingredient_value[i]
        new_value.append(myround(old_value * ingredient_multiple, 2))

    print(f'Matcha Mousse Cake Ingredients( {size_now} inch) are as follow:')  
    print_part('Part 1 (Chiffon Cake ): ', 'Mousse')   
    print_part('Part 2 (Mousse Paste ): ', 'Cake')
