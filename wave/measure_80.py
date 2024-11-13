import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

height = 80
args = np.array([-3.97919147e-05, 2.43326460e-02, -5.70464209e+00, 5.11065306e+02])
data = pd.read_csv(f'measure_{height}.csv', header=None).to_numpy()
t_exp = float(data[1][0])
t_o = float(data[2][0])


def lin_ls(x, y):
    k = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
    b = np.mean(y) - k * np.mean(x)
    k_s = (len(x) ** (-0.5)) * (((np.mean(y ** 2) - np.mean(y) ** 2) / (
                np.mean(x ** 2) - np.mean(x) ** 2) - k ** 2) ** 0.5)
    b_s = k_s * ((np.mean(x ** 2) - np.mean(x) ** 2) ** 0.5)
    return (k, k_s, b, b_s)


stop_index = np.where(data[0] == 159)[0][0]
index = int(t_o / t_exp * len(data[0])) + 1
y = np.polyval(args, data[0])
x = np.array([i / len(data[0]) * t_exp for i in range(len(data[0]))]) - t_o
y = y[index:stop_index]
x = x[index:stop_index]
b1 = np.mean(y[:64])
k2, d_k2, b2, d_b2 = lin_ls(x[64:], y[64:])

t_res = (b1 - b2) / k2

plt.figure(dpi=100)
plt.plot(x, y)
plt.plot(x, np.array([b1] * len(x)), color='orange')
plt.plot(x, k2 * x + b2, color='green')
plt.axvline(t_res, color='red', linestyle='--')
plt.ticklabel_format(style='sci',
                     axis='both',
                     scilimits=(0, 0),
                     useMathText=True)

plt.minorticks_on()

plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7')
plt.grid(visible=True,
         which='minor',
         linestyle='-',
         linewidth=1,
         color='0.8')

plt.xlim([0, np.max(x) * 1.05])
plt.ylim([np.min(y) * 0.95, np.max(y) * 1.05])

plt.title(f'Зависимость уровня воды \n в кювете от времени')
plt.text(0.1, float(np.min(y)),
         f'L = 1.2 м \n'
         f't = {round(t_res, 2)} с \n'
         f'H_0 = {round(b1, 2)} мм \n'
         f'v = {round(1.2 / t_res, 2)} м/с',
         bbox=dict(facecolor='white', alpha=0.75, edgecolor='white'))
plt.xlabel(r"$ Время, с$")
plt.ylabel(r"Уровень воды, мм")

plt.show()
