# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, work_in_h, stavka_in_h, premia = argv
print(f"заработная плата составляет:{(float(work_in_h) * float(stavka_in_h)) + float(premia)}")
