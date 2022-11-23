
from typing import Any, List, TypeVar
from py_config_stack_thealpinegoat.events import kStackFullError




class StackError(BaseException):
    pass


T = TypeVar("T")

class Stack:
    def __init__(self, initial: List[T], max_size: int = 0):
        self._data: List[T] = initial
        self._max_size: int = max_size

    @property
    def top(self) -> T:
        return self._data[-1]

    @property
    def empty(self) -> bool:
        return len(self._data) == 0

    @property
    def size(self) -> int:
        return len(self._data)

    def push(self, element: T) -> None:
        if self.size < self._max_size:
            self._data.append(element)
        else:
            raise StackError(kStackFullError)

    def emplace(self, element: T) -> None:
        # TODO: implement this
        pass

    def pop(self) -> T:
        return self._data.pop(-1)

    def swap(self) -> None:
        # TODO: implement this
        pass

    # TODO: implement operators
    # TODO: implement __str__ and __repr__
