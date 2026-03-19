import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# funskjonen fra oppgaven
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# ligningen vi skal løse
def equation(x):
    return np.arctan(x) - 4/(x**2 + 1)

# Finn løsning (startverdi 1)
x_max = fsolve(equation, 1)[0]
y_max = f(x_max)

print("Toppunkt: ")
print("x = ", round(x_max, 4))
print("y = ", round(y_max, 4))

# plott
x =np.linspace(0, 5, 100)
y = f(x)

plt.plot(x, y)
plt.scatter(x_max, y_max) # Marker toppunkt
plt.title("f(x) = e^(-x/4) * arctan(x)")
plt.show()