proceed = "y"
while proceed == "y":
    numb1 = float(input("Введите первое число: "))
    sing = input("Введите операцию ")
    numb2 = float(input("Введите второе число "))
    if sing == "+":
        print(numb1 + numb2)
    elif sing == "-":
        print(numb1 - numb2)    
    elif sing == "*":
        print(numb1 * numb2)
    elif sing == "/":
        print(numb1 / numb2) 
    else:
        print("Введите правильный оператор: плюс, минус, умножение, деление.")
    proceed = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить ")