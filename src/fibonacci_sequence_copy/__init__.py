from typing import Any
import pandas as pd
import matplotlib.pyplot as plt

class HelperMaths:

    @classmethod
    def to_list(cls, n1 ,n2):
        """
            Makes sure given arguments are floats and are returned as list
        """
        n1 = float(n1)
        n2 = float(n2)

        return [n1, n2]


class Viewer:
    pass


class Sequences:
    _list_of_sequences: list = []

    """

    ```python
    # Return list of all created sequences
    .get_all[index]


    ```
    """
    @classmethod
    def get_all(cls):
        return cls._list_of_sequences

    @classmethod
    def count(cls):

        return len(cls._list_of_sequences)

    """
    ### .count

        - Gets how many sequences
    """
    

    @classmethod
    def add(cls, new_sequence):
        """
        Add new sequence to the _list_of_sequences
        """
        cls._list_of_sequences.append(new_sequence)

class FibonacciSequence:
    
    def __init__(self, *,
                 starts_with: tuple[float, float],
                 length = 10) -> None:
        """
            Creates fibonacci sequence object
        """

        self._sequence = HelperMaths.to_list(*starts_with)
        self._initial_numbers = self.sequence[0:2]
        self._length = length

        self.populate()
        Sequences.add(self)

    def __call__(self, starts_with: tuple[float, float], length = 10) -> Any:

        self.__class__(starts_with = starts_with, length = length)
        return self.__class__


    def populate(self):
        
        sliding_window = [0, 1]

        while sliding_window[1] < self.length-1:
            
            left, right = sliding_window

            n1 = self.sequence[left] # left number from sliding window
            n2 = self.sequence[right] # right number from sliding window

            # Add to sequence
            # Round to 6 decimal places to get round floating point approximation
            self.sequence = round(n1 + n2, 6)

            # Move sliding window 1 index to the right
            sliding_window[0] += 1
            sliding_window[1] += 1

            

    @property
    def sequence(self):
        return self._sequence
    
    @sequence.setter
    def sequence(self, val):
        self._sequence.append(val)
    
    @sequence.deleter
    def sequence(self):
        del Sequences
        del self

    @property
    def initial(self):
        """
        .initial

        - Returns initial values given to a sequence
        """
        return self._initial_numbers
    @property
    def length(self):
        return self._length
    @property
    def count(self):
        return len(self._sequence)