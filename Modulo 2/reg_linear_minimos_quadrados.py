#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = [4.3, 4.5, 5.9, 5.6, 6.1, 5.2, 3.8, 2.1, 7.5]
y = [126, 121, 116, 118, 114, 118, 132, 141, 108]

# y = ax + b
# y = a1x + a0

plt.plot(x, y, 'o', color='black')
plt.ylabel('Partículas removidas (Mg / m3)')
plt.xlabel('Chuvas diárias (0,01 cm)')
plt.show()

x = np.array(x, dtype="float64")
y = np.array(y, dtype="float64")

n = x.shape[0]

Sx = 0
Sy = 0
Sxy = 0
Sx2 = 0

for i in range(n):
    Sx += x[i]
    Sy += y[i]
    Sxy += x[i] * y[i]
    Sx2 += x[i] * x[i]

# médias
avg_x = Sx / n
avg_y = Sy / n

a1 = (n*Sxy - Sx*Sy ) / (n*Sx2 - Sx*Sx)
a0 = avg_y - a1*avg_x





# %%
