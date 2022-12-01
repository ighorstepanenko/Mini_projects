import random


def proverka(x):
    while not x.isdigit() or int(x) < 1:
        x = input('Пожалуйста, введи натуральное число: ')
    x = int(x)
    return x


def dobavlenie(z):
    while z.lower() not in ['да', 'нет']:
        z = input('Немного не понял тебя. Пожалуйста, напиши "Да" либо "Нет": ')
    if z.lower() == 'да':
        flag = True
    else:
        flag = False
    return flag

def get_password(x, y, z):
    parol = []
    for _ in range(x):
        c = ''
        for _ in range(y):
            c += random.choice(z)
        parol.append(c)
    parol = '\n'.join(parol)
    return parol
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = []

print('Привет! Давай придумаем для тебя безопасный пароль. Для этого укажи, пожалуйста, пожелания к нему.')

kolichestvo = input('Сколько паролей для тебя сгенерировать: ')
kolichestvo = proverka(kolichestvo)
dlina = input('Из скольки символов должен состоять пароль: ')
dlina = proverka(dlina)
digits = input('Скажи, должен ли твой пароль включать цифры (0123456789)? Ответь "Да" или "Нет": ')
if dobavlenie(digits):
    chars.extend(DIGITS)
lowercase_letters = input(
    'Теперь напиши, должен ли твой пароль включать строчные буквы (abcdefghijklmnopqrstuvwxyz)? Ответь "Да" или "Нет": ')
if dobavlenie(lowercase_letters):
    chars.extend(LOWERCASE_LETTERS)
uppercase_letters = input('А заглавные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? Ответь "Да" или "Нет": ')
if dobavlenie(uppercase_letters):
    chars.extend(UPPERCASE_LETTERS)
punctuation = input(
    'Осталось немного. Подскажи, включить в пароль специальные символы (!#$%&*+-=?@^_)? Ответь "Да" или "Нет": ')
if dobavlenie(punctuation):
    chars.extend(PUNCTUATION)
iskluchenie = input('Исключить ли из пароля неоднозначные символы (il1Lo0O)? Ответь "Да" или "Нет": ')
if dobavlenie(iskluchenie):
    del chars[chars.index('i')]
    del chars[chars.index('l')]
    del chars[chars.index('1')]
    del chars[chars.index('L')]
    del chars[chars.index('o')]
    del chars[chars.index('0')]
    del chars[chars.index('O')]
print(f'Готово! Вот варианты паролей: \n{get_password(kolichestvo, dlina, chars)}')