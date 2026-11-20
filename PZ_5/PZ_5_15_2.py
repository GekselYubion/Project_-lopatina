# 1. Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно 
# разрезать данный прямоугольник, если от него каждый раз отрезать квадрат
# наибольшей площади.



def square(a,b):
    count = 0
    while a > 0 and b > 0:
        if a >= b:
            a = a - b
            count += 1
        else:
            b = b - a
            count += 1
    print(count)

while True:
    try:
        a = int(input("число а "))
        b = int(input("число b "))
        break
    except ValueError:
        print("только числа ")

square(a,b)