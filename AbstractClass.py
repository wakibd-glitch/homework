from abc import ABC,abstractmethod

class myclass(ABC):
    def print(self, x):
        print("Passed value is: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class newclass(myclass):
    def task(self):
        print("We are inside newclass")

class newclass(myclass):
    def task(self):
        print("We are inside newclass")


test_obj = newclass()

test_obj.task()
test_obj.print(100)