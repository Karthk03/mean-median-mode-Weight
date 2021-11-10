import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#mean

sum = 0
noOfVal = len(new_data)
for val in new_data:
    sum+=val

mean = sum/noOfVal
print(mean)

#median

if(noOfVal%2==0):
    median1 = float(new_data[noOfVal//2])
    median2 = float(new_data[(noOfVal//2)-1])

    median = (median1+median2)/2
    print(median)
else:
    median = new_data[noOfVal//2]
    print(median)

# mode
new_dataInt = []
for x in range(len(file_data)):
    n_num = file_data[x][3]
    new_dataInt.append(int(n_num))

data = Counter(new_dataInt)
item = data.items()

mode,modef = 0,0

for y in item:
    tempMode,tempModef = y
    if(tempModef>modef):
        modef = tempModef
        mode = tempMode

print(mode)