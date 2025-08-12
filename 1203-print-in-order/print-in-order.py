import threading as th
from typing import Callable

class Foo:
    def __init__( self ):
        self.first_call = th.Event()
        self.second_call = th.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_call.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_call.wait()
        printSecond()
        self.second_call.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_call.wait()
        printThird()