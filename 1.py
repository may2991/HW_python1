# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("for_1.txt", "w") as f_1:
    k = 1
    while True:
        str = input(f"введите {k}-ю строку. Об окончании ввода данных свидетельствует пустая строка.\n")
        if not str:
            break
        f_1.writelines(str)
        f_1.writelines('\n')
        k += 1


