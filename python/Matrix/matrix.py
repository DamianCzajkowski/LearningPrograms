from exceptions import MatrixIndexException, MatrixOperationException
from matrixiterator import MatrixIterator, MatrixRowsIterator, MatrixColsIterator
from collections.abc import Iterable


class Matrix(Iterable):

    def __init__(self, n: int, m: int):
        self._n = n
        self._m = m
        self._matrix = self._generate_matrix(n=self._n, m=self._m)
    
    def _generate_matrix(self, n: int, m: int) -> list:
        matrix = []
        for row in range(n):
            matrix.append([])
            for _ in range(m):
                matrix[row].append(0)
        return matrix

    def _validate_indexes(self, r: int, c: int) -> bool:
        if r >=0 and r < self._n and c>=0 and c < self._m:
            return True
        else:
            return False
    
    def getNumberOfRows(self) -> int:
        return self._n
    
    def getNumberOfCols(self) -> int:
        return self._m
    
    def get_value(self, r: int, c: int) -> float:
        """get value from matrix

        Args:
            r (int): number of row
            c (int): number of column
            value (float): value to put in matrix

        Raises:
            MatrixIndexException: if indexes are not in allowed range

        Returns:
            float: value from matrix
        """
        if self._validate_indexes(r, c):
            return self._matrix[r][c]
        else:
            raise MatrixIndexException()
    
    def set_value(self, r: int, c: int, value: float()) -> None:
        """In python set is a builtin class so i changed it to set_value

        Args:
            r (int): number of row
            c (int): number of column
            value (float): value to put in matrix

        Raises:
            MatrixIndexException: if indexes are not in allowed range
        """
        if self._validate_indexes(r, c):
            self._matrix[r][c] = value
        else:
            raise MatrixIndexException()

    def _compare_matrix_sizes_to_add(self, other_matrix):
        if self.getNumberOfRows() == other_matrix.getNumberOfRows() and \
           self.getNumberOfCols() == other_matrix.getNumberOfCols():
            return True
        else:
            return False
    
    def _compare_matrix_sizes_to_multiply(self, other_matrix):
        if self.getNumberOfRows() == other_matrix.getNumberOfCols():
            return True
        else:
            return False
    
    def __str__(self):
        list_of_strings = []
        for row in range(self.getNumberOfRows()):
            list_of_strings.append(" ".join(str(value) for value in self._matrix[row]))
        return "\n".join(list_of_strings)
    
    def __add__(self, other_matrix):
        if self._compare_matrix_sizes_to_add(other_matrix):
            result = Matrix(self.getNumberOfRows(), self.getNumberOfCols())
            for row in range(self.getNumberOfRows()):
                for col in range(self.getNumberOfCols()):
                    value = self.get_value(r=row, c=col) + other_matrix.get_value(r=row, c=col)
                    result.set_value(r=row, c=col, value=value)
            return result
        else:
            raise MatrixOperationException
    
    def __mul__(self, other_matrix):
        if self._compare_matrix_sizes_to_multiply(other_matrix):
            result = Matrix(self.getNumberOfRows(), other_matrix.getNumberOfCols())
            for i in range(self.getNumberOfRows()):
                for j in range(other_matrix.getNumberOfCols()):
                    value = 0
                    for k in range(other_matrix.getNumberOfRows()):
                        value += self.get_value(r=i, c=k) * other_matrix.get_value(r=k, c=k)
                    result.set_value(r=i, c=j, value=value)
            return result
        else:
            raise MatrixOperationException
    
    def __iter__(self):
        return MatrixIterator(self._matrix)

    def rows(self):
        return MatrixRowsIterator(self._matrix)
    
    def cols(self):
        return MatrixColsIterator(self._matrix)
