# Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K
# . Найти
# целое число K — показатель этой степени.
while type:
    try:
        n = int(input("n "))
        k = 0 
        break
    except ValueError:
        print("только числа")
while n>1:
    n= n // 2
    k += 1
print(k)
