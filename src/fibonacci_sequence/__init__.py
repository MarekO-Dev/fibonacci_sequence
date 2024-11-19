from typing import Any
import pandas as pd

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
        
        new_sequence: dict = {}
        
        start = 0
        end = 1

        for _ in self.initial_sequence:
            
            try:
                
                if not reversed:

                    ratio = (second := self.initial_sequence[end]) / (first := self.initial_sequence[start])
                else:
                    ratio = (second := self.initial_sequence[start]) / (first := self.initial_sequence[end])
                new_sequence[f"({first:_^8.0f} {second:_^8.0f})"] = ratio
            except ZeroDivisionError:
                new_sequence[f"({first:_^8.0f} {second:_^8.0f})"] = 0

            start += 1
            end += 1

            if end >= len(self.initial_sequence):
                break

        return new_sequence
    
    @property
    def ratios_df(self):

        series_values = pd.Series(self.ratios_dict().keys())
        series_ratios = pd.Series(self.ratios_dict().values())
        
        return pd.DataFrame({"Numbers": series_values, "Ratio": series_ratios})

    @property
    def ratios_df_reversed(self):
        
        series_values = pd.Series(self.ratios_dict(reversed = True).keys())
        series_ratios = pd.Series(self.ratios_dict(reversed = True).values())
        
        return pd.DataFrame({"Numbers": series_values, "Ratio": series_ratios})