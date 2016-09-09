'''
def rsp(mine,yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try:
    rsp('가위','바')
except ValueError:
    print('값이 이상합니다.')
'''
school = {'1반': [172, 185, 199, 177, 160, 179, 162],
    '2반': [165, 177, 164, 152, 166, 177,195]}

try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print(class_number,'반에 190을 넘는 학생이 있다.')
                #raise StopIteration
except StopIteration:
    print('정상종료')