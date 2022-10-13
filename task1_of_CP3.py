name = input("Введите своё имя: ")
surname = input("Введите свою фамилию: ")
dob = int(input("Введите свой год рождения: "))

print(name, surname, dob, sep="_")
name, surname = surname, name
dob += 60
print(name, surname, dob, sep="_")
