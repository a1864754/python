import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))
X = np.linspace(0, 2 * np.pi, 100, endpoint=True)
sin, cos, log, exp = np.sin(X), np.cos(X), np.log(X), np.exp(X)

plt.figure(figsize=(10, 5))
plt.figure(1)
ax1 = plt.subplot(221)
plt.plot(X, sin, linestyle='--', color='red')
ax2 = plt.subplot(222)
plt.plot(X, cos)
ax3 = plt.subplot(223)
plt.plot(X, log)
ax4 = plt.subplot(224)
plt.plot(X, exp)

plt.show()
