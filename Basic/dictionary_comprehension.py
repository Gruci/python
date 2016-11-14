students = ["태연", "진우", "하늘", "가인"]

for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다'.format(number,name))

students_dict = {"{}번".format(number + 1): name for number, name in enumerate(students)}

print(students_dict)

score = ['22', '100', '88', '57']

score_dict = {students: score for students, score in zip(students,score)}

print(score_dict)