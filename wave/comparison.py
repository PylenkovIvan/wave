import numpy as np
import matplotlib.pyplot as plt


def lin_ls(x, y):
    k = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
    b = np.mean(y) - k * np.mean(x)
    k_s = (len(x) ** (-0.5)) * (((np.mean(y ** 2) - np.mean(y) ** 2) / (
                np.mean(x ** 2) - np.mean(x) ** 2) - k ** 2) ** 0.5)
    b_s = k_s * ((np.mean(x ** 2) - np.mean(x) ** 2) ** 0.5)
    return (k, k_s, b, b_s)


y = np.log(np.array([0.48, 0.7, 0.86, 1.1, 1.18, 1.15]))
x = np.log(np.array([19.41, 39.52, 58.84, 80.09, 100.18, 115.05]) / 1000)
k, d_k, b, d_b = lin_ls(x, y)

plt.figure(dpi=100)
plt.plot(x, y, 'o')
line = np.array(range(-10, 10))
plt.plot(line, k * line + b, color='blue', label='эксперимент')
plt.plot(line, line * 0.5 + 0.5 * np.log(9.81), color='orange', label='теория')
print(k, d_k, b, d_b)
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

plt.xlim([np.min(x) * 1.05, np.max(x) * 0.95])
plt.ylim([np.min(y) * 1.15, np.max(y) * 1.15])

plt.title(f'Сравнение экспериментальных и  \n теоретических данных')
plt.text(np.min(x), 0,
         f'k = {round(k, 2)} \n'
         f'd_k = {round(d_k, 2)} \n'
         f'b = {round(b, 2)} \n'
         f'd_b = {round(d_b, 2)}',
         bbox=dict(facecolor='white', alpha=0.75, edgecolor='white'))
plt.ylabel(r"$ ln(v)$")
plt.xlabel(r"0.5ln(h) + 0.5ln(g)")
plt.legend()

plt.show()
