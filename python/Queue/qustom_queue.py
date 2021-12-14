from typing import TypeVar, Generic, List

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get(self) -> T:
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def isEmpty(self) -> bool:
        return not bool(len(self.items))
