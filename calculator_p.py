num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))

choice = input("Выберите операцию /, *, +, - : ")

if choice == "/":
    if num2 == 0:
        print("На ноль делить нельзя")
    else:
        print(num1 / num2)
elif choice == "*":
    print(num1 * num2)
elif choice == "-":
    print(num1 - num2)
elif choice == "+":
    print(num1 + num2)
else:
    print(f"Неизвестная операция!: {choice}")