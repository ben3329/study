#단일 인터페이스 제공을 통해 서브 시스템 접근을 용이하게 함
#시스템 설계 시 모든 클래스, 객체의 연관관계 알아야 함
#클래스간 의존도는 최소화 해야하

class EventManager(object):
    def __init__(self):
        print("Event Manager!!")
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        self.caterer = Caterer()
        self.caterer.setCuisine()
        self.musician = Musician()
        self.musician.setMusicType()

class Hotelier(object):
    def __init__(self):
        print("Arrange the Hotel")
    def __isAvailable(self):
        print("Is Free")
        return True
    def bookHotel(self):
        if self.__isAvailable():
            print("Register")

class Florist(object):
    def __init__(self):
        print("Flower Deco")
    def setFlowerRequirements(self):
        print("carnation, Roses...")

class Caterer(object):
    def __init__(self):
        print("Food arrange")
    def setCuisine(self):
        print("Chinese,..")

class Musician(object):
    def __init__(self):
        print("Musical Arrange")
    def setMusicType(self):
        print("Jazz..")

class You(object):
    def __init__(self):
        print("You")
    def askEventManager(self):
        print("Contact Manager")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("done")

you = You()
you.askEventManager()

