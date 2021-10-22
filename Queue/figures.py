from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def label(self) -> None:
        pass

    @abstractmethod
    def getLabel(self) -> str:
        pass


class Point(Figure):

    def __init__(self, label):
        self.label = label

    def label(self, label) -> None:
        self.label = label

    def getLabel(self) -> str:
        return self.label

    def __str__(self) -> str:
        return f"Class: {self.__class__.__name__}, Params = label: {self.label}"


class Circle(Figure):

    def __init__(self, label):
        self.label = label

    def label(self, label) -> None:
        self.label = label

    def getLabel(self) -> str:
        return self.label

    def __str__(self) -> str:
        return f"Class: {self.__class__.__name__}, Params = label: {self.label}"
