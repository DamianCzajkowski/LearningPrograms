from itertools import chain
from collections.abc import Iterator


class MatrixIterator(Iterator):
    _position: int = None

    def __init__(self, matrix):
        self._matrix = list(chain.from_iterable(zip(*matrix)))
        self._position = 0
    
    def __next__(self):

        try:
            value = self._matrix[self._position]
            self._position += 1
        except:
            raise StopIteration()
        return value


class MatrixRowsIterator(Iterator):

    def __init__(self, matrix):
        self._matrix = matrix
        self._position = 0
    
    def __next__(self):

        try:
            value = self._matrix[self._position]
            self._position += 1
        except:
            raise StopIteration()
        
        return value

class MatrixColsIterator(Iterator):

    def __init__(self, matrix):
        self._matrix = list(zip(*matrix))
        self._position = 0
    
    def __next__(self):

        try:
            value = self._matrix[self._position]
            self._position += 1
        except:
            raise StopIteration()
        
        return value