# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:16:35 2020

@author: Tejaswini...!
"""

#to take and add two numbers
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
add=a+b
print("addition of two numbers is:",add)

#to prompt a user for their name and welcome them
name=input("enter name:")
print("welcome",name)

#to prompt the user to compute gross pay
h=input("number of hours:")
r=input("rate per hour:")
gp=float(h)*float(r)
print("gross pay is",gp)

#assume that we execute the following assignment statements
width=17
height=12.0
a=width//2
print(a , type(a))
b=width//2.0
print(b , type(b))
c=height/3
print(c , type(c))
d=1+2*5
print(d , type(d))

#to prompt the user for celcius temperature,convert to farenheit and print theconverted temperature
t=float(input("enter temp in celcius:"))
f=float(t*1.8)+32
print("entered temp is equal to", f, "farenheit")