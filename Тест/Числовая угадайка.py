from random import *

print('Добро пожаловать в числовую угадайку')


def proverka(number, diap):
    return number.isdigit() and 1 <= int(number) <= diap


def prover_di(z):
    while not z.isdigit():
        z = input('Пожалуйста, введите число:')
    return int(z)


def game():
    diapazon = input('Какое максимальное число мы можем загадать (оно должно быть больше 1)?')
    diapazon = prover_di(diapazon)
    zagadannoe = randint(1, diapazon)
    flag, counter, vvedennoe = True, 0, input(f'Как вы думаете, какое число от 1 до {diapazon} мы загадали:')
    while flag:
        counter += 1
        if not proverka(vvedennoe, diapazon):
            print(f'А может быть все-таки введем целое число от 1 до {diapazon}?')
            vvedennoe = input('Попробуйте снова:')
            continue
        vvedennoe = int(vvedennoe)
        if vvedennoe < zagadannoe:
            print('Не-а, мы загадали число, большее этого')
            vvedennoe = input('Попробуйте ещё раз:')
        elif vvedennoe > zagadannoe:
            print('Загаданное нами число меньше')
            vvedennoe = input('Новая попытка:')
        else:
            print('Вы угадали, поздравляем! Количество попыток:', counter)
            flag = False


def snova():
    print('Хотите сыграть снова? Введите "д", если хотите, и "н",  если не хотите')
    n = input()
    if n.lower() == 'д':
        game()
    elif n.lower() != 'н':
        print('Пожалуйста, введите "д" либо "н"')
    return n


game()

while snova() != 'н':
    snova()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
