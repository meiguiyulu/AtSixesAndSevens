import matplotlib.pyplot as plt


base = [350, 500, 800, 1000, 3000, 5000, 8000]

x = [i for i in range(20 * 12)]

for cost in base:
    total = cost * 3 + 3000
    average = total / 139 + 162
    y = []
    for month in x:
        y.append(average * month - total)
    plt.plot(x, y)

plt.show()
