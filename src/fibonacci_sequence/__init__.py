from typing import Any
import pandas as pd

class SequenceItem:

    def __init__(self, seq: tuple) -> None:
        self.items = dict()

    def __call__(self, ) -> Any:
        pass

class FibonacciSequence:
    def __init__(self,
                 initial_sequence: tuple[float, float] = (float(0), float(1)),
                 *,
                 limit: int = 20) -> None:
        
        self.initial_sequence: list = list(initial_sequence)
        self.limit: int = (limit - len(self.initial_sequence)) - 1

    def __call__(self, 
                 printout = False) -> Any:

        values_index = 0

        # For every value in sequence list 
        for _ in self.initial_sequence:
            
            # Get the sum of initial numbers and continue moving index to get next ones
            sum = float(self.initial_sequence[(values_index)])\
                  + float(self.initial_sequence[(values_index + 1)])
            
            # Add the sum to the sequence
            self.initial_sequence.append(float(sum))

            if values_index >= self.limit:
                break

            values_index += 1
        
        if printout:

            for val in self.initial_sequence:
                print(f"{float(val):.^20.4f}")

        return self

    def ratios_dict(self, *, reversed: bool = False) -> dict:
        
        _new_sequence: dict = {
            "Number1": [],
            "Number2": [],
            "Ratio": []
        }
        
        _start: int = 0
        _end: int = 1

        for _ in self.initial_sequence:
            
            try:
                
                if not reversed:

                    ratio = (second := self.initial_sequence[_end]) / (first := self.initial_sequence[_start])
                else:
                    ratio = (second := self.initial_sequence[_start]) / (first := self.initial_sequence[_end])
                
                _new_sequence["Number1"].append(first)
                _new_sequence["Number2"].append(second)
                _new_sequence["Ratio"].append(ratio)
                
            except ZeroDivisionError:

                _new_sequence["Number1"].append(first)
                _new_sequence["Number2"].append(second)
                _new_sequence["Ratio"].append(0)

            _start += 1
            _end += 1

            if _end >= len(self.initial_sequence):
                break

        return _new_sequence
    
    def _get_dict(self, reversed = False):

        ratios_dict = self.ratios_dict(reversed = reversed)

        series_numbers1 = pd.Series(ratios_dict["Number1"])
        series_numbers2 = pd.Series(ratios_dict["Number2"])
        series_ratios = pd.Series(ratios_dict["Ratio"])
        
        return pd.DataFrame({"Number1": series_numbers1, "Number2": series_numbers2, "Ratio": series_ratios})

    @property
    def ratios_df(self):

        return self._get_dict()

    @property
    def ratios_df_reversed(self):
        
        return self._get_dict(reversed = True)