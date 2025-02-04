import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = threading.Lock()
        self.foo_turn = threading.Condition(self.foolock)
        self.bar_turn = threading.Condition(self.foolock)
        self.is_foo_turn = True


    def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                with self.foolock:
                    while not self.is_foo_turn:
                        self.foo_turn.wait()
                    printFoo()
                    self.is_foo_turn = False
                    self.bar_turn.notify()
            
             #outputs "foo". Do not change or remove this line


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
            for i in range(self.n):
                with self.foolock:
                    while self.is_foo_turn:
                        self.bar_turn.wait()
                    printBar()
                    self.is_foo_turn = True
                    self.foo_turn.notify()
            
            # printBar() outputs "bar". Do not change or remove this line.