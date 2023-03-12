import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

base = [350, 500, 800, 1000, 3000, 5000, 8000]

x = [i for i in range(20 * 12)]

for cost in base:
    total = cost * 3 + 3000
    average = total / 139 + 162
    y = []
    for month in x:
        y.append(average * month - total)
    plt.plot(x, y)
    plt.scatter(x, y)


plt.xlabel("月份")
plt.ylabel("金额")
plt.show()
