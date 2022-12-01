with open(r'C:\Users\ighor\Downloads\population.txt', encoding='utf-8') as file:
    for line in file:
        s = line.split('\t')
        if s[0][0] == 'G' and int(s[1]) > 500000:
            print(s[0])