#!/usr/bin/env python3
# Copyright 2018 Lulu Wang

# e.g.01
a = [1,1,0,1]
b = [1,1,1]

# e.g.02
#a = [0,1,1,0,1]
#b = [1,1,0]

# e,g.03
#a = [1,0,0,1,0,1,0,1,1,1,0,0,0,1,0]
#b =             [0,1,0,1,1,0,0,1,0]

# e,g.04
#a =             [0,1,0,1,1,0,0,1,0]
#b = [1,0,0,1,0,1,0,1,1,1,0,0,0,1,0]

addl  = list()
addlr = list()
maxl  = list()
minl  = list()

a_length = len(a)
b_length = len(b)
lenmax   = max(a_length,b_length)  #
lenmin   = min(a_length,b_length)  #
lengap   = lenmax - lenmin         #

if a_length >= b_length:
    maxl = a
    minl = b   
else:
    maxl = b
    minl = a 

def addBit(bit1, bit2):
    if  bit1 == 1 and bit2 == 1:
        carry = 1
        new_value = 0
    else:
        carry = 0
        new_value = bit1 ^ bit2

    return [new_value, carry]

def addBitWithCarry(bit1, bit2, input_carry):
    new_value, carry = addBit(bit1, bit2)

    if input_carry == 0:
        return [new_value, carry]

    after_carry_new_value, after_carry_new_carry = addBit(new_value, 1)

    if carry == 1 or after_carry_new_carry == 1:
        final_carry = 1
    else:
        final_carry = 0

    return [after_carry_new_value, final_carry]

carry = 0

for p in range(lenmin):

    maxl_value = maxl[lenmax - 1 - p]
    minl_value = minl[lenmin - 1 - p]

    x_value, carry = addBitWithCarry(maxl_value, minl_value, carry)

    addlr.append(x_value)
#    print(f'maxl,minl,addlr = {i,j,k}:{maxl[i],minl[j],addlr[k]}: "(key  = {key[k]})" addlr = {addlr}')

for i in range(lengap-1,-1,-1):
    maxl_value = maxl[i]

    x_value, temp = addBit(maxl_value, carry)
    addlr.append(x_value)

    if carry == 1:      
        if maxl_value == 1 and i == 0:
            addlr.append(1)

    carry = temp


print(f'maxlist = {maxl}')

space = ''
for i in range(lengap):
    space_0 = '   '
    space = space + space_0

print(f'minlist = {space}{minl}')


for i in reversed(addlr):
    addl.append(i)
print(f'addl    = {addl}')

#notes:
# 1. addlr.append(x_value)
