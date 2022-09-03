# 동일 리소스에 대한 동시 요청 시 충돌 방지
# 전역변수 값이 변경되었는지 확인 어려움
# 많은 참조자
# 전역변수 수정 시 모든 종속 클래스에 영향을  미침

#normal singleton
print("========normal========")
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)

#Lazy instantiation
#필요할 때 생성
print("========Lazy========")
class SingletonLazy:
    __instance = None
    def __init__(self):
        if not SingletonLazy.__instance:
            print("__init__method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance    

s = SingletonLazy()
print("object created", SingletonLazy.getInstance())
s1 = SingletonLazy()

#Mono singleton
#상태만 공유
print("========Mono========")
class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)
print("Object State 'b': ", b.__dict__)
print("Object State 'b1': ", b1.__dict__)

print("========Mono new========")
class BorgNew(object):
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(BorgNew, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

b = BorgNew()
b1 = BorgNew()
b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)
print("Object State 'b': ", b.__dict__)
print("Object State 'b1': ", b1.__dict__)

#using Meta class
#singleton 많이 쓸 때 좋을 듯
print("========Meta========")
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()

print(logger1, logger2)

#example
print("========Example1========")
import sqlite3
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)

print("========Example2========")
class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []
    
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])