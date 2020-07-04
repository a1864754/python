import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print(matplotlib.matplotlib_fname())

csv_data = pd.read_csv("iris.csv")
print(csv_data)

fig = plt.figure(figsize=(15, 8))
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
sns.set(style="ticks")
ax = fig.add_subplot(211)
sns.swarmplot(x="sepal_length", y="sepal_width", data=csv_data, hue="species")
# plt.xlabel("花瓣长度") # x轴名称
# plt.ylabel("花瓣宽度") # y 轴名称
ax = fig.add_subplot(212)
sns.swarmplot(x="petal_length", y="petal_width", data=csv_data, hue="species")
# plt.xlabel("花萼长度") # x轴名称
# plt.ylabel("花萼宽度") # y 轴名称
plt.show()
