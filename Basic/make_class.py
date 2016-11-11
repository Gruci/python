class Human():
    '''사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = '영어'

person1.name = '서울시민'
person2.name = '미쿡인'

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name,person.language))

"""
    speak(person1)
    speak(person2)
    같은 형식으로 함수 사용
"""

Human.speak = speak

person1.speak()
person2.speak()


def create_human(name,weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.crete = create_human

person = Human.crete("철수",60.5)

def eat(person):
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(person.name,person.weight))

def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(person.name,person.weight))

Human.walk = walk
Human.eat = eat

person.walk()
person.eat()