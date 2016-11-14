class Animal():

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("{}이/가 인사한다".format(self.name))


class Human(Animal):#자바의 상속

    def __init__(self,name,hand):
        super().__init__(name)
        self.hand = hand
    
    def wave(self):
        print("{} 손을 흔들면서".format(self.hand))
    
    def greet(self):
        self.wave()
        super().greet()

class Cow(Animal):
    ''''''

class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다")

    def greet(self):
        self.wag()

person = Human("사람","오른손")
person.walk()
person.eat()
person.wave()
person.greet()

dog = Dog("개")
dog.walk()
dog.eat()
dog.wag()
dog.greet() #부모의 greet를 override했다

cow = Cow("소")
cow.greet()
