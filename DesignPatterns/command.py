# 작업을 요청하는 클래스와 수행하는 클래스가 분리됨
# 커맨드 추가 용이
# 클래스, 객체 많아짐
class Wizard():
    def __init__(self, src, rootdir) -> None:
        self.choices = []
        self.rootdir = rootdir
        self.src = src
    def preferences(self, command):
        self.choices.append(command)
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copybin -- ", self.src, 'to', self.rootdir)
            else:
                print('no op')
if __name__ == '__main__':
    wizard = Wizard('py.gzip', '/usr/bin')
    wizard.preferences({'py':True})
    wizard.preferences({'java':False})
    wizard.execute()

from abc import ABC, ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def __init__(self, recv) -> None:
        self.recv = recv
    def execute(self):
        pass
class ConcreteCommand(Command):
    def __init__(self, recv) -> None:
        self.recv = recv
    def execute(self):
        self.recv.action()
class Receiver:
    def action(self):
        print('recv action')
class Invoker:
    def command(self, cmd):
        self.cmd = cmd
    def execute(self):
        self.cmd.execute()

if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
    

from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock) -> None:
        self.stock = stock
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock) -> None:
        self.stock = stock
        
    def execute(self):
        self.stock.sell()
        
class StockTrade:
    def buy(self):
        print('buy')
    def sell(self):
        print('sell')
        
class Agent:
    def __init__(self) -> None:
        self.__orderQueue = []
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()
        
if __name__ == '__main__':
    #client
    stock = StockTrade()
    buystock = BuyStockOrder(stock)
    sellstock = SellStockOrder(stock)
    #invoker
    agent = Agent()
    agent.placeOrder(buystock)
    agent.placeOrder(sellstock)