# Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму
# 1 + A + A2 + A3 + ... + AN

while type:
    try:
        a= int(input("введите число а"))
        n= int(input("введите число n (>0)"))
        count = 0
        summ = 1
        break
    except ValueError:
        print("только числа ")

while n > count:
    count += 1
    summ +=a**count
print(summ)
