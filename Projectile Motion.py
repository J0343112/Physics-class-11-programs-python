import os 
import sys
import math

pi= 22/7 

i=int(input("your angle:"))

ri= i*22/7
ip= ri/180

print("Angle in radian :{:.2f}".format(ip))

rri=math.sin(ip)
print("sin({}) = {:.2f}".format(i,rri))
