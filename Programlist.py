print("Вы попали в тестовую программу по роботе со списками")
l = input("Введите желаемый список: ")

while True:
    op = input("Выберети операцию, которую хотите проделать над списком: \n1 - Посчитать количество символов в списке. \n2 - Привести список к верхнему регистру. \n3 - Привести список к нижнему регистру. \n4 - Добавить значение в конец списка. \n5 - Выход из программы. \n")
    if  op.isdigit() and "1" <= op <= "5":
        if op == "1":
            print(len(l))
            quit = input("Хотите выйти? (Да-'y'/Нет-'n')\n")
            if quit == "y":
                print("Программа завершена")
                break
            elif quit == "n":
                continue 
        elif op == "2":
            print(l.upper())
            quit = input("Хотите выйти? (Да-'y'/Нет-'n')\n")
            if quit == "y":
                print("Программа завершена")
                break
            elif quit == "n":
                continue    
        elif op == "3":
            print(l.lower())
            quit = input("Хотите выйти? (Да-'y'/Нет-'n')\n")
            if quit == "y":
                print("Программа завершена")
                break
            elif quit == "n":
                continue   
        elif op == "4":
            l1 = input("Введите цифры для буквы для добавления в список:\n")
            print(l + l1)
            quit = input("Хотите выйти? (Да-'y'/Нет-'n')\n")
            if quit == "y":
                print("Программа завершена")
                break
            elif quit == "n":
                continue   
        elif op == "5":
            quit = input("Хотите выйти? (Да-'y'/Нет-'n')\n")
            if quit == "y":
                print("Программа завершена")
                break
            elif quit == "n":
                continue 
print("Спасибо, что протестировали нашу программу:)")
                



