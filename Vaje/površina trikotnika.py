from math import *
a = float(input("Dolžina stranice a? "))
b = float(input("Dolžina stranice b? "))
c = float(input("Dolžina stranice c? "))
pt = (sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a)))/4
print("Površina trikotnika:",pt)
s = (a+b+c)/2
pvk = pi * (s-a) * (s-b) * (s-c) /s
print("Površina včrtanega kroga:",pvk)
pok = pi * (a*b*c/4/pt)**2
print("Površina očrtanega kroga:",pok)




