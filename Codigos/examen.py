from math import *

ec = input("Ingresa la ecuacion a resolver")
xa = float(input("Ingresa el inicial inferior"))
xb = float(input("Ingresa el inicial superior"))
tol = float(input("Ingresa la tolerancia"))

def f(x):
    return eval(ec)

iter = 0
f_c = 999

while abs(f_c) >= tol:
    pM = (xa+xb)/2
    f_a = f(xa)
    f_b = f(xb)
    f_c = f(pM)

    iter += 1
    print("x_a: ",xa," x_b: ",xb, " c: ",pM," f_c: ",f_c, " Iteraciones: ",iter)

    if (f_a * f_c) < 0:
        xb = pM
    elif (f_b * f_c) < 0:
        xa = pM
    
    if abs(f_c) < tol:
        break

print("La raiz buscada es: ",pM)
