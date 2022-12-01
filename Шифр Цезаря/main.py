def proverka_way(n):
    while n.lower() not in ['з', 'д']:
        n = input('Немного не понял. Пожалуйста, используй "З" либо "Д": ')
    return n


def proverka_lang(z):
    while z.lower() not in ['р', 'а']:
        z = input('Пожалуйста, используй "Р" либо "А": ')
    return z


def proverka_step(x):
    if language == 'р':
        if x in [0, 32]:
            x = input('Мы получим тот же текст, введи число от 1 до 31(включительно): ')
            proverka3(x)
        elif x not in range(1, 32):
            x = input('Используй число от 1 до 31(включительно): ')
            proverka3(x)
    else:
        if x in [0, 26]:
            x = input('Мы получим тот же текст, введи число от 1 до 25(включительно): ')
            proverka3(x)
        elif x not in range(1, 26):
            x = input('Используй число от 1 до 25(включительно): ')
            proverka3(x)
    return x


def rez(ac, la, st, te):
    result = ''
    for i in te:
        if i.isalpha() and i.isupper():
            if ac == 'з':
                if la == 'р':
                    result += upper_rus_alphabet[(upper_rus_alphabet.find(i) + st) % 32]
                else:
                    result += upper_eng_alphabet[(upper_eng_alphabet.find(i) + st) % 26]
            elif la == 'р':
                result += upper_rus_alphabet[upper_rus_alphabet.find(i) - st]
            else:
                result += upper_eng_alphabet[upper_eng_alphabet.find(i) - st]
        elif i.isalpha():
            if ac == 'з':
                if la == 'р':
                    result += lower_rus_alphabet[(lower_rus_alphabet.find(i) + st) % 32]
                else:
                    result += lower_eng_alphabet[(lower_eng_alphabet.find(i) + st) % 26]
            elif la == 'р':
                result += lower_rus_alphabet[lower_rus_alphabet.find(i) - st]
            else:
                result += lower_eng_alphabet[lower_eng_alphabet.find(i) - st]
        else:
            result += i
    return result


upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
print('Привет! Давай изменим текст с помощью Шифра Цезаря.')
action = input('Скажи, ты хочешь зашифровать или дешифровать текст? Напиши "З" или "Д": ')
action = proverka_way(action).lower()
language = input('На каком языке будет твой текст? "Р" - русский, "А" - английсский: ')
language = proverka_lang(language).lower()
step = int(input('С каким шагом сдвига будем работать? Укажи цифру: '))
step = proverka_step(step)
text = input('Введи текст: ')
print(f'Готово, получился такой резуьтат: {rez(action, language, step, text)}')
