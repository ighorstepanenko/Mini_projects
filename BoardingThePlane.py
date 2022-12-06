# Решение задачи "В самолете n рядов и по три кресла слева и справа в каждом ряду. Крайние кресла (A и F) находятся у окна, центральные (C и D) – у 
# прохода. На регистрацию приходят группы из одного, двух или трех пассажиров. Они желают сидеть рядом, то есть на одном ряду и на одной стороне: левой 
# или правой. Например, группа из двух пассажиров может сесть на кресла B и C, но не может сесть на кресла C и D, потому что они разделены проходом, 
# а также не может сесть на кресла A и C, потому что тогда они окажутся не рядом. Кроме того, один из пассажиров каждой группы очень требовательный – 
# он хочет сесть либо у окна, либо у прохода. Конечно же, каждая группа из пассажиров хочет занять места в ряду с как можно меньшим номером, ведь 
# тогда они скорее выйдут из самолета после посадки. Для каждой группы пассажиров определите, есть ли места в самолете, подходящие для них.
    
    
def rassadka(x, y, z, o):
    spisok = mesta.copy()
    if y != '.' * len(y):
        return False
    print('Passengers can take seats: ', end='')
    for q in o:
        c.append(f'{spisok.index(j) + 1}{q}')
    print(*c, end='\n')
    spisok[spisok.index(j)] = x + 'X' * len(y) + z
    print(*spisok, sep='\n', end='\n')
    mesta[mesta.index(j)] = x + '#' * len(y) + z
    global flag
    flag = False
    return True


mesta = [input() for _ in range(int(input()))]
passengers = [tuple(input().split()) for _ in range(int(input()))]
bukvi = ('A', 'B', 'C', '_', 'D', 'E', 'F')
for i in passengers:
    c = []
    flag = True
    if i[1] == 'left':
        for j in mesta:
            if i[2] == 'aisle':
                if rassadka(j[:3 - int(i[0])], j[3 - int(i[0]):3], j[3:], bukvi[3 - int(i[0]):3]):
                    break
                else:
                    continue
            else:
                if rassadka('', j[:int(i[0])], j[int(i[0]):], bukvi[:int(i[0])]):
                    break
                else:
                    continue
    else:
        for j in mesta:
            if i[2] == 'aisle':
                if rassadka(j[:4], j[4: 4 + int(i[0])], j[4 + int(i[0]):], bukvi[4: 4 + int(i[0])]):
                    break
                else:
                    continue
            else:
                if rassadka(j[:7 - int(i[0])], j[7 - int(i[0]):], '', bukvi[7 - int(i[0]):]):
                    break
                else:
                    continue
    if flag:
        print('Cannot fulfill passengers requirements', end='\n')
