import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.fill_between(x, y1, y2, where=(y1 > y2), color='orange')
plt.fill_between(x, y1, y2, where=(y1 < y2), color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
