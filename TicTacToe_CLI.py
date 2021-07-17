# optional multi time play without clear screen
b = {7: ' ', 8: ' ', 9: ' ',
     4: ' ', 5: ' ', 6: ' ',
     1: ' ', 2: ' ', 3: ' '}


def printsampleboard():
    for i in range(1,10):
        b[i] = ' '
    print()
    print()
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
    print('-----------')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('-----------')
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
    print()


def printboard():
    print()
    print(' ' + b[7] + ' | ' + b[8] + ' | ' + b[9])
    print('-----------')
    print(' ' + b[4] + ' | ' + b[5] + ' | ' + b[6])
    print('-----------')
    print(' ' + b[1] + ' | ' + b[2] + ' | ' + b[3])
    print()


def evaluate(c):
    if (b[7] == b[8] == b[9] == c) or \
            (b[4] == b[5] == b[6] == c) or \
            (b[1] == b[2] == b[3] == c) or \
            (b[7] == b[4] == b[1] == c) or \
            (b[8] == b[5] == b[2] == c) or \
            (b[9] == b[6] == b[3] == c) or \
            (b[7] == b[5] == b[3] == c) or \
            (b[9] == b[5] == b[1] == c):
        return c
    else:
        return ''


def celebration(c):
    if c == '':
        print()
        print('.....D R A W.....')
        print()
    else:
        print()
        print('.....', c, 'WON.....')
        print()


again = 1
while again == 1:
    winner = ''
    i = 0
    printsampleboard()
    print('numbers points to the corresponding slots in the board\n')
    while i <= 8:
        if i % 2 == 0:
            p = 'X'
        else:
            p = 'O'
        pos = int(input(p + ' : '))
        if not (1 <= pos <= 9):
            print('wrong input')
            i -= 1
        elif b[pos] != ' ':
            print('already filled')
            i -= 1
        else:
            b[pos] = p
            printboard()
            winner = evaluate(p)
        if winner != '':
            break
        i += 1
    celebration(winner)
    again = int(input('enter 1 to play again    (any other will Quit the game)  : '))
