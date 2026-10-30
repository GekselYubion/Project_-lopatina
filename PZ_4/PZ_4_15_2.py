# Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K
# . Найти
# целое число K — показатель этой степени.
while True:
    try:
        n = int(input("n "))
        if n < 0:
            print("число должно быть больше 0")
            continue
        break
    except ValueError:
        print("только числа")
k = 0 
while n>1:
    n= n // 2
    k += 1
print(f"пкоазатель степени k= {k} ")
