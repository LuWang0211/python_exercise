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
key   = list()
keyr  = list()

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

for i, j, k in zip(range(lenmax-1,-1,-1), range(lenmin-1,-1,-1), range(lenmin)):
    maxl_value = maxl[i]
    minl_value = minl[j]

    if i == lenmax-1:
        if  maxl_value & minl_value == 1:
            temp = 1
            x_value = 0
        else:
            temp = 0
            x_value = maxl_value ^ minl_value
        key.append(temp)
    else:  
        if key[k-1] == 1:
            if maxl_value == 0 and minl_value == 0:
                temp = 0
                x_value = 1
            elif maxl_value == 1 and minl_value == 1:
                temp = 1
                x_value = 1
            else:
                temp = 1
                x_value = 0
        else:
            if maxl_value == 1 and minl_value == 1:
                temp = 1
                x_value = 0
            else:
                temp = 0
                x_value = maxl_value ^ minl_value
        key.append(temp)

    addlr.append(x_value)
#    print(f'maxl,minl,addlr = {i,j,k}:{maxl[i],minl[j],addlr[k]}: "(key  = {key[k]})" addlr = {addlr}')

for i in range(lengap-1,-1,-1):
    maxl_value = maxl[i]
    key_length = len(key)
    if key[key_length-1] == 1:
        if maxl_value == 1:
            temp = 1
            x_value = 0
            if i == 0:
                addlr.append(x_value)
                addlr.append(1)
            else:
                addlr.append(x_value)
        else:
            temp = 0
            x_value = 1
            addlr.append(x_value)        
    else:
        temp = 0
        x_value = maxl_value
        addlr.append(x_value)
    key.append(temp)



print(f'maxlist = {maxl}')

space = ''
for i in range(lengap):
    space_0 = '   '
    space = space + space_0

print(f'minlist = {space}{minl}')

for i in reversed(key):
    keyr.append(i)
print(f'keyr    = {keyr}')

for i in reversed(addlr):
    addl.append(i)
print(f'addl    = {addl}')

#notes:
# 1. addlr.append(x_value)
