def hangman(word):
    wrong = 0
    stages = ['',
             '___________           ',
             '|          |          ',
             '|          |          ',
             '|          O          ',
             '|         /|\         ',
             '|          |          ',
             '|         / \         ',
             '|'
             ]
    rletters = list(word)#引数wordを１文字ずつの要素に分解してリストにする
    board = ['*']*len(word)
    win = False
    print('ハングマンへようこそ！')

    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字予想してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print('回答「',' '.join(board),'」')
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '*' not in board:
            print('\n')
            print('あなたの勝ち！')
            print('回答「', ' '.join(board), '」')
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！ 正解は「{}」'.format(word))

import random

answer = ['cat', 'dog', 'wolf', 'rhino', 'gorilla']

hangman(random.choice(answer))