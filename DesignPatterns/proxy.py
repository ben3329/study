# 복잡한 시스템을 간단하게 표현
# 객체에 대한 보안 제공
# 메모리 핸들링
# Proxy: RealSubject에 대한 Client 접근 제어
# Subject: RealSubject 와 Proxy의 인터페이스
# RealSubject: 실 객체

class Actor(object):
    def __init__(self):
        self.isBusy = False
    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied")
    def available(self):
        self.isBusy = False
        print(type(self).__name__, "if free")
    def getStatus(self):
        return self.isBusy

class Agent(object):
    def __init__(self):
        self.principal = None
    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    r = Agent()
    r.work()

# Virtual Proxy
# 무거운 객체의 플레이스 홀더 역할.
# Remote Proxy
# 원격 서버나 다른 주소 공간에 존재하는 객체에 대한 로컬 인스턴스 생성
# Protective Proxy
# RealSubject의 중요한 부분에 대한 접근 제어
# Smart Proxy
# 사용자가 객체에 접근했을 때 추가적인 행동 수행

from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __hasFunds(self):
        print("Bank:: Checking if Account ", self.__getAccount(), "enough")
        return True
    def setCard(self, card):
        self.card = card
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: paying")
            return True
        else:
            print("Bank:: fail...")
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = 'qwer'
        self.bank.setCard(card)
        return self.bank.do_pay()   

class You:
    def __init__(self):
        print("You:: Buy")
        self.debitCard = DebitCard()
        self.isPurchased = None
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    def __del__(self):
        if self.isPurchased:
            print("You:: good")
        else:
            print("You:: fail")

you = You()
you.make_payment()