# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    Z=int(input("Введите количество карандашей: "))
    O=int(input("Введите количество ручек: "))
    V=int(input("Введите количество фломастеров: "))
    cena_karandash=3
    cena_ruchki=cena_karandash+2
    cena_flomastera=cena_ruchki+7
    vsego=(Z*cena_karandash)+(O*cena_ruchki)+(V*cena_flomastera)
    print("Общая стоимость покупки:",vsego)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()