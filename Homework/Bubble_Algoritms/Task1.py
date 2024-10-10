ls = [1, 7, 4, 9, 3, 2, 10, 8, 6]

for i in range(len(ls) - 1):
    for j in range(len(ls) - i - 1):
        if ls[j] > ls[j + 1]:
            ls[j],ls[j + 1] = ls[j + 1],ls[j]

ls1 = ls
print(ls1)