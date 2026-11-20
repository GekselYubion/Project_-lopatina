# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов

def str(n):
    print(n*"#")
while True:
    try:
        n = int(input("число "))
        break
    except ValueError:
        print("только число")
str(n)


    