import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
import math
sns.set()

t = np.linspace(0, 100, 1000)
x = [0, 0]
delta = 0.15
k = 7
m = 12
omega = math.sqrt(k/m)
A = 0.1


def sho1(t, x):
    result = [x[1], (-2 * delta * x[1] - (k / m) * x[0] + A * math.sin(0.5*omega*t))]
    return result

def sho2(t, x):
    result = [x[1], (-2 * delta * x[1] - (k / m) * x[0] + A * math.sin(1*omega*t))]
    return result

def sho3(t, x):
    result = [x[1], (-2 * delta * x[1] - (k / m) * x[0] + A * math.sin(2*omega*t))]
    return result


solution1 = solve_ivp(sho1, [0, 1000], y0=x, t_eval=t)
solution2 = solve_ivp(sho2, [0, 1000], y0=x, t_eval=t)
solution3 = solve_ivp(sho3, [0, 1000], y0=x, t_eval=t)
plt.plot(t, solution1.y[0], 'orange', label="0.5$\omega$")
plt.plot(t, solution2.y[0], 'green', label="1$\omega$")
plt.plot(t, solution3.y[0], 'blue', label="2$\omega$")
plt.legend(loc="upper left")
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator z tłumieniem i z wymuszeniem', fontsize=20)
plt.grid(True)
plt.show()
