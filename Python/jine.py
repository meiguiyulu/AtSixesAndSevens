

base = [350, 500, 800, 1000, 3000, 5000, 8000]

x = [i for i in range(20 * 12)]

for cost in base:
    print(cost, end=":\t")
    total = cost * 3 + 3000
    average = total / 139 + 162
    y = []
    for month in x:
        print(average * month - total, end="\t")
    print()

if __name__ == '__main__':

    fw = open("deal.txt", 'w')  # 将要输出保存的文件地址

    for month in x:
        fw.write(str(month) + "月份")
        fw.write("\t")

    fw.write("\n")

    for cost in base:
        print(cost, end=":\t")
        total = cost * 3 + 3000
        average = total / 139 + 162
        y = []
        for month in x:
            fw.write((str(average * month - total)))
            fw.write("\t")
        fw.write("\n")



