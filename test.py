def summa(*args):
    s = 0
    for i in args:
        s += i
    print('Сумма равна ',s)
    

summa(5, 6, 7, 87, 756)

def say_hello(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

say_hello(Иван='Иванов', Петя='Петров')