def f(m, t):
    g = 9.8
    c = 15
    return (g * m / c) * (1 - 2.71828 ** (-c * t / m)) - 35


def falsa_posicion(f, a, b, es=0.1, imax=100):
    count = 0
    for i in range(imax):
        fa, fb = f(a, 9), f(b, 9)
        c = b - (fb * (a - b)) / (fa - fb)
        fc = f(c, 9)
        count+=1
        print ("Iteración: ", count, "=", c)
        if abs(fc) < es:
            break

        if fc * fa < 0:
            b = c
        else:
            a = c

    return c


# Intervalo [a, b]
a, b = 50, 60

# Llamada al método de la falsa posición
raiz_aproximada = falsa_posicion(f, a, b)
print("Raíz aproximada (masa m):", raiz_aproximada)