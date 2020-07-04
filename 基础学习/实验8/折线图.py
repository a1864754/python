import matplotlib.pyplot as plt
import numpy as np

month = np.linspace(1, 9, 9)
# print(month)
user_num = [886, 2335, 5710, 6482, 6120, 1605, 3813, 4428, 4631]

print(plt.style.available)
plt.figure(figsize=(10, 5))
plt.style.use('fivethirtyeight')
plt.rcParams['font.sans-serif'] = ['STSong']
plt.title("某公司1-9月用户注册量")
plt.figure(1)
plt.plot(month, user_num,
         color="red",
         linestyle="--",
         linewidth=2,
         marker='o',
         markersize=10)
plt.legend('注册用户数')
for a, b in zip(month, user_num):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=15)

plt.show()
