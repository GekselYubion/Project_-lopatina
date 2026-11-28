# Дан целочисленный список размера n, 
# все элементы которого упорядочены (по возрастанию или по убыванию). Найти количество различных элементов в данном списке
a = list(map(int ,input("введите число  n ").split()))
a.sort(key=None , reverse=True)
n = len(a)

count = 1
for i in range(1, n):
    if a[i] != a[i - 1]:
        count += 1

print(count)
