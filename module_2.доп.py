n = int(input('Введите число от 3 до 20, иначе помрете: '))
result = []
for i in range(1, 20):
    for j in range(i+1, 20):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)
        else:
            continue
print(*result)