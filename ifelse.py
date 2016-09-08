SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이김'
DRAW = '비김'
LOSE = '짐'

mine = '가위'
yours = '바위'

if mine == yours:
    result = DRAW

else:
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else:
            result = WIN
    
    elif mine == ROCK:
        if yours == PAPER:
                result = LOSE
        else:
                result = WIN

    elif mine == PAPER:
        if yours == SCISSOR:
                result = LOSE
        else:
                result = WIN
    else:
        print('??')

print(result)