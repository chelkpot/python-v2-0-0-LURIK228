# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    Z,O,V=map(int,input().split())
    cena_karandash=3
    cena_ruchki=cena_karandash+2
    cena_flomastera=cena_ruchki+7
    vsego=(Z*cena_karandash)+(O*cena_ruchki)+(V*cena_flomastera)
    print(vsego)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()