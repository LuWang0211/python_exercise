#!/usr/bin/env python3
# Copyright 2018 Lulu Wang

import math
#6 inch cake ingredients
size_original = 6

Cake_eggs = 3 
Cake_oil = 25
Cake_suger = 60
Cake_matcha = 1
Cake_salt = 1
Cake_milk = 60
Cake_flour = 60

Mouse_gelatine = 2
Mouse_matcha = 1
Mouse_milk = 125
Mouse_sugar = 70
Mouse_cream = 175
Mouse_cheese = 100

size_request = input('How big is the cake you want? ')  #Prompt

size = ('6','8','9','10','11','12')  # cake size optipn
auth = False
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

while (size_request not in size):
    count +=1
    if count > max_attempt: 
        print('You entered more than 3 times and you cannot try more')
        break
    size_request = input(f"Sorry, we don't have this cake size, could you change the cake size?({count} times) ")
else:
    auth = True
    size_now = size_request
    ingredient_multiple = int(size_now) ** 2 / size_original **2
    ingredient_multiple = float(ingredient_multiple)

    Cake_eggs_now = myround(Cake_eggs * ingredient_multiple,2)
    Cake_oil_now = myround(Cake_oil * ingredient_multiple,2)
    Cake_suger_now = myround(Cake_suger * ingredient_multiple,2)
    Cake_matcha_now = myround(Cake_matcha * ingredient_multiple,2)
    Cake_salt_now = myround(Cake_salt * ingredient_multiple,2)
    Cake_milk_now = myround(Cake_milk * ingredient_multiple,2)
    Cake_flour_now = myround(Cake_flour * ingredient_multiple,2)


    Mouse_gelatine_now =  myround(Mouse_gelatine * ingredient_multiple,2)
    Mouse_matcha_now =  myround(Mouse_matcha * ingredient_multiple,2)
    Mouse_milk_now =  myround(Mouse_milk * ingredient_multiple,2)
    Mouse_sugar_now = myround(Mouse_sugar * ingredient_multiple,2)
    Mouse_cream_now = myround(Mouse_cream * ingredient_multiple,2)
    Mouse_cheese_now = myround(Mouse_cheese * ingredient_multiple,2)

    print(f'Matcha Mousse Cake Ingredients( {size_now} inch) are as follow:')
    print(f'Part 1 (Chiffon Cake ): {Cake_eggs_now} eggs, {Cake_oil_now}g vegetable oil, {Cake_suger_now}g sugar, {Cake_matcha_now} tbsp matcha powder, {Cake_salt_now} pinch of salt, {Cake_milk_now}g milk, {Cake_flour_now}g cake flour')
    print(f'Part 2 (Mousse Paste ): {Mouse_gelatine_now} slices of Gelatine, {Mouse_matcha_now}tbsp matcha powder, {Mouse_milk_now}g milk, {Mouse_sugar_now}g sugar, {Mouse_cream_now}g cream, {Mouse_cheese_now}g mascarpone cheese')
