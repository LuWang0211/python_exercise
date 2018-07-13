#!/usr/bin/env python3
# Copyright 2018 Lulu Wang

import math

class mymath:                               #My floor and ceil
    def myfloor(self):                        
        newself = self // 1
        return(int(newself))                #return the largest integer less than or equal to x   

    def myceil(self):                      
        newself = self // 1
        if newself != self:
            newself = self // 1 + 1
        else:
            newself = self
        return(int(newself))                #return the smallest integer greater than or equal to x           

x= [-10.9, -6.5, -4 , -2.4, -0.1, 0, 0.1, 1, 2.4, 6.5, 10.9]    #original list

length = len(x)                              #demonstration
pythonnew_xf = list()
pythonnew_xc = list()
mynew_xf = list()
mynew_xc =list()

for i in range(length):
    x_value = x[i]
    pythonnew_xf.append(math.floor(x_value))     #python floor calculate
    pythonnew_xc.append(math.ceil(x_value))      #python ceil calculate
    mynew_xf.append(mymath.myfloor(x_value))     #my floor calculat
    mynew_xc.append(mymath.myceil(x_value))      #my ceil calculat

print(f'x = {x}')
print(f'{"python math.floor results: pythonnew_xf":<40} = {pythonnew_xf}')    #show result list
print(f'{"my math.floor results: mynew_xf":<40} = {mynew_xf}')
print(f'{"python math.ceil results: pythonnew_xc":<40} = {pythonnew_xc}')
print(f'{"my math.ceil results: mynew_xc":<40} = {mynew_xc}')
