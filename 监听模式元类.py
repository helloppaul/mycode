from abc import ABCMeta,abstractmethod
# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
class Observer(metaclass=ABCMeta):
    """观察者元类"""
    @abstractmethod
    def update(self,ovservable,object):
        pass

class Observable:
    """被观察者元类"""
    def _init_(self):
        self.__observers=[]

    def addObservers(self,observer):
        self.__observers.append(observer)

    def removeObservers(self,observer):
        self.__observers.remove(observer)

    def notifyObservers(self,object=0):
        for o in self.__observers:
            o.udpate(self,object)
