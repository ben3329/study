# 메인 객체 메소드를 사용해 서브 객체를 메인 객체에 등록 후 메인 객체에서 서브 객체의 메소드 사용
# subject와 observer의 느슨한 결합 추구
# 장점
# 객체 간 수정, 추가, 삭제 자유로움
# 단점: 컴포지션 선택권 없음
# 풀 모델
# subject 변경사항을 observer에 브로드캐스트
# observer는 subject에게 변경 사항을 요청하여 가져옮
# 푸시 모델
# subject가 observer에게 데이터 전송
class Subject:
    def __init__(self) -> None:
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1:
    def __init__(self, subject) -> None:
        subject.register(self)
        
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)
        
class Observer2:
    def __init__(self, subject) -> None:
        subject.register(self)
        
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)
        
subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll('noti')

class NewsPublisher:
    def __init__(self) -> None:
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()
        
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addNews(self, news):
        self.__latestNews = news
    
    def getNews(self):
        return "Got News:", self.__latestNews
    
from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):
    
    @abstractmethod
    def update(self):
        pass

class SMSSubscriber:
    def __init__(self, publisher) -> None:
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber:
    def __init__(self, publisher) -> None:
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

if __name__ == '__main__':
    new_publisher = NewsPublisher()
    for subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscriber(new_publisher)
    print('\nSubs:', new_publisher.subscribers())
    
    new_publisher.addNews('Hello')
    new_publisher.notifySubscribers()

    print('\ndetach:', type(new_publisher.detach()).__name__)
    print('\nsubs:', new_publisher.subscribers())
    
    new_publisher.addNews('2nd')
    new_publisher.notifySubscribers()
