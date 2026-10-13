import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 400)
y = 2 * x + np.sin(x) ** 2 + 3

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("po.pdf")
plt.show()
