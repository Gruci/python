a = 10
if a < 0 and 2 ** a > 1000 and a % 5 == 2 and round(a) == a:
    print('복잡한 식')

def return_false():
    print('함수 return_false')
    return False

def return_true():
    print('함수 return_true')
    return True

print('테스트1')

a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)

print('테스트2')

if return_false() and return_true(): #뒤의 return_true()가 실행이 안된다
    print('True')
else:
    print('False')