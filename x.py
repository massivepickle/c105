import pandas as pd
import statistics
import csv

with open("c105/d.csv",newline="") as f:
    reader = csv.reader(f)
    arr1 = list(reader)

arr = arr1[0]

mean = 0

for x in arr:
    mean += int(x)

mean = mean/len(arr)

newarr = []

for i in arr:
    value = (int(i) - int(mean))**2
    newarr.append(value)

sum = 0

for j in newarr:
    sum += j

div1 = sum/(len(newarr)-1)

squareroot = div1**(1/2)

print(squareroot)