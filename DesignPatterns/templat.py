# 상속을 사용한 패턴
# 장점: 코드 중복 없음, 알고리즘의 각 단계를 서브 클래스에서 구현하는 유연성 제공
# 단점: 디버깅, 유지보수 어려움

from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass
    @abstractmethod
    def compileToObject(self):
        pass
    @abstractmethod
    def run(self):
        pass
    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):
    def collectSource(self):
        print('col sw sc')
    def compileToObject(self):
        print('com sw to ob')
    def run(self):
        print('run')

iOS = iOSCompiler()
iOS.compileAndRun()

from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def operation1(self):
        pass
    @abstractmethod
    def operation2(self):
        pass
    def template_method(self):
        print('def algo')
        self.operation2()
        self.operation1()

class ConcreteClass(AbstractClass):
    def operation1(self):
        print('op1')
    def operation2(self):
        print('op2')

class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()

client = Client()
client.main()

from abc import abstractmethod, ABCMeta

class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass
    @abstractmethod
    def day1(self):
        pass
    @abstractmethod
    def day2(self):
        pass
    @abstractmethod
    def day3(self):
        pass
    @abstractmethod
    def returnHome(self):
        pass
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()

class VeniceTrip(Trip):
    def setTransport(self):
        print('take boat')
    def day1(self):
        print('visist st')
    def day2(self):
        print('aaaa bbbb')
    def day3(self):
        print('enjoy 3')
    def returnHome(self):
        print('go back')

class MaldivesTrip(Trip):
    def setTransport(self):
        print('on foot')
    def day1(self):
        print('enjoy 1')
    def day2(self):
        print('hahahahaha')
    def day3(self):
        print('relax')
    def returnHome(self):
        print('homeeeeeeee')

class TravelAgency:
    def arrange_trip(self):
        choice = input('aaa or bbb')
        if choice == 'aaa':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'bbb':
            self.trip = MaldivesTrip()
            self.trip.itinerary()
            
TravelAgency().arrange_trip()