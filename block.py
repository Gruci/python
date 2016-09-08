if True:
    print('블럭에 속한 코드')
    print('들여쓰기가 똑같아야 문법 오류가 나지 않는다')
    if True:
        print('블럭안의 블럭')
    print('블럭의 끝')

print('블럭을 끝마치려면 들여쓰기를 지우면 된다')

if False:
    print('틀린 블럭에 속한 코드')
    if True:
        print('블럭안의 블럭')
    print('블럭의 끝')