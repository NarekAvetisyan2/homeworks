ls = [40, 80, 90, 30, 10, 50, 60, 70, 100, 20]

for i in range(len(ls)):
    min_index = i
    for j in range(len(ls) - 1 ):
        if ls[j] > ls[min_index]:
            min_index = j
            ls[min_index], ls[i] = ls[i], ls[min_index]


ls1 = ls
print(ls1)
