# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов

def strr(n):
    print(n*"#")
while True:
    try:
        n = int(input("число "))
        break
    except ValueError:
        print("только число")
strr(n)


    