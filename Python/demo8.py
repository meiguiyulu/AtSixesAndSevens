import pandas as pd

base = [350, 500, 800, 1000, 3000, 5000, 8000]

months = [i for i in range(20 * 12)]

all_result = []

for cost in base:
    total = cost * 3 + 3000
    average = total / 139 + 162
    y = []
    for month in months:
        y.append(average * month - total)
    all_result.append(y)

# print(all_result)

info_marks = pd.DataFrame({'350': all_result[0],
                           '500': all_result[1],
                           '800': all_result[2],
                           '1000': all_result[3],
                           '3000': all_result[4],
                           '5000': all_result[5],
                           '8000': all_result[6],
                           }).T
print(info_marks)
# render dataframe as html
writer = pd.ExcelWriter('output2.xlsx')
info_marks.to_excel(writer)
writer.save()
print('DataFrame is written successfully to the Excel File.')
