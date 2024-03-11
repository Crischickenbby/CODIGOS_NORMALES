import numpy as np
import matplotlib.pyplot as plt

g = 9.8
m = 68.1
c = 12.5
# Primera parte de tu código con el bucle
for t in range(0, 12, 2):
    v = g * m / c * (1 - np.exp((-c / m) * t))
    print(v)

# Segunda parte de tu código con la gráfica
t = np.arange(0, 50, 5)
v = g * m / c * (1 - np.exp((-c / m) * t))

plt.plot(t, v, color="red")
plt.xlabel("t")
plt.ylabel("v")
plt.title("v=g*m/c(1-np.exp((-c/m)*t))")
plt.grid()
plt.show()