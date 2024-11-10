secret_word = input('Введите слово для игры: ').lower()
print('\033[2J')
win = False
all_letters = []
true_letters = []
points = [0, 0, 0]  
counter = 0 

while not win:
    letter = input('\nИгрок в {counter + 1} ведите букву: ').lower()
    if letter in all_letters:
        print(f'Вы уже вводили букву "{letter}"')
    elif letter in secret_word:
        win = True
        print(f'Вы угадали букву "{letter}"!')
        points[counter] += 1
        print(f'Ваши очки: {points[counter]}')
        true_letters.append(letter)
    else:
        print(f'Буквы {letter} нет в слове!')
        
    all_letters.append(letter)

    for symbol in secret_word:
        if not symbol in true_letters:
            print('*', end='')
            win = False
        else:
            print(symbol, end='')

    counter += 1
    if counter == 3:
        counter = 0 

winner = points.index(max(points)) + 1
print(f"""
Игра окончена!
Слово: {secret_word}

Очки игроков:
Игрок 1: {points[0]}
Игрок 2: {points[1]}
Игрок 3: {points[2]}

Победитель - Игрок {winner}!""")
