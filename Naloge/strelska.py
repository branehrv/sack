from math import *
v = int(input("Hitrost izstrelka v m/s je "))
kot = int(input("Pod kotom v stopinjah "))
kot_rad = radians(kot)
g = 9.81
S = v**2 * sin(2*kot_rad) / g
print("Dolzina izstrelka je",S,"metrov")

