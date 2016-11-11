class Human():
    '''사람'''
    def __init__(self, name, weight):
        '''초기화 함수'''
        self.name = name
        self.weight = weight
        #print("__init__실행")
        #print("이름은 {} 몸무게는 {}".format(name,weight))
        #인스턴스를 만들떄 바로 호출되는 함수 = 별도의 create 호출 없이 생성
    
    def __str__(self):
        '''문자열화함수'''
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
        #해당 인스턴스를 출력 할 때의 형식을 지정

    '''
    def create(name,weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person
    '''

    def eat(self):
        person.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name,self.weight))

    def walk(self):
        person.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name,self.weight))

    def speak(self, message):
        print(message)

person = Human("사람", 60)
print(person)
print(person.name)
print(person.weight)

#person = Human.create("철수", 60.5)

#person.eat()
#person.speak("안녕하세요")