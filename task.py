import csv
file = open("data.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()
rows = []
headers = ['date', 'city', 'value']
print(data)
print(data[0][0])
x = 0
list = []
for i in range(1, len(data)):
    for x in range (1,len(data[i])):
        list.append(data[0][i])
        list.append(data[i][0])
        list.append(data[i][x])
        rows.append(list)
        list = []
print(rows)

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(rows)