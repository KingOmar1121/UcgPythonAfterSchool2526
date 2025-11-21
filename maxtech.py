list = [73,18,92,47,6,54,81,35,67,28,99,12,43,60,77,25,89,31,9,50]
max_value = max(list)
print(max_value)   
for i in list:
    if i == max_value:
        print("Index of max value:", list.index(i))
   