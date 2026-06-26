# часть первая. print(), sep, end, f-strings
print("Привет, мир!")
print(f"{5} {10} {15}")
print(10+25)
print(1, 2, 3, sep="&")
print("Python", end=" ")
print("Python")
x, y = 3.14, -8
print(f"Координаты точки: x = {x}; y = {y}")

# часть вторая. input() и преобразование типов
name = input("Введите имя: ")
print(f"Привет, {name}!")
age = int(input("Подскажите ваш возраст: "))
print(f"Имя: {name}, Возраст: {age}")
x, y = [int(input()) for _ in "xy"]
print(x+y)
print(int(input())**2)
print(2*(float(input()) + float(input())))

# булевые значения
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
res = 8 > 12
print(res, type(res))
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print(x % 3 == 0 and x % 5 == 0)
y = 4.5
print(1 <= y <= 10)
print(0 <= y <= 5 or 10 <=y <= 15)
print(not y < 5)
print(bool(0), bool(-5), bool(3.14), bool(""), bool("Python"), bool(" "), sep="\n")

# Часть четвертая. Индексы и срезы строк
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2])
print(s[-2])
print(s[:6])
print(s[-5:])
print(s[2:7])
print(s[::2])
print(s[::-1])
print(s[1:-1])

# Часть 5. Неизменяемость строк
# s[0] = "п"

s2 = "П" + s[1:]
print(s2)