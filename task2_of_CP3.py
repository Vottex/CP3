a = float(input("Первый катет: "))
b = float(input("Второй катет: "))
S = 0.5*a*b
P = a + b + (a**2+b**2)**0.5
print("Площадь = ", S)
print("Периметр = ", P)