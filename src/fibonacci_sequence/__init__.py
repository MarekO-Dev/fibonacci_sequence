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
    
    def printout_sequence_ratio(self):
        
        for k, v in self.return_ratios_dict.items():
            try:
                print(f"{k:^30}", " ratio is ", f"{v:^30}")
            except TypeError:
                print(f"{k:^30}", " ratio is ", f"{'ZERO':^30}")

    @property
    def return_sequence(self) -> list:
        
        """
            ### Return sequence as list
        """

        return self.initial_sequence

    @property
    def ratios_list(self) -> list:
        
        new_sequence: list = []
        
        start = 0
        end = 1

        for _ in self.initial_sequence:
            
            try:
                ratio = self.initial_sequence[end] / self.initial_sequence[start]
                new_sequence.append(ratio)
            except ZeroDivisionError:
                new_sequence.append(None)

            start += 1
            end += 1

            if end >= len(self.initial_sequence):
                break

        return new_sequence
    
    @property
    def ratios_dict(self) -> dict:
        
        new_sequence: dict = {}
        
        start = 0
        end = 1

        for _ in self.initial_sequence:
            
            try:
                ratio = (second := self.initial_sequence[end]) / (first := self.initial_sequence[start])
                new_sequence[f"({first:^8.0f}, {second:^8.0f})"] = ratio
            except ZeroDivisionError:
                new_sequence[f"({first:^8.0f}, {second:^8.0f})"] = 0

            start += 1
            end += 1

            if end >= len(self.initial_sequence):
                break

        return new_sequence

    @property
    def ratios_dict_reversed(self) -> dict:
        
        new_sequence: dict = {}
        
        start = 0
        end = 1

        for _ in self.initial_sequence:
            
            try:
                ratio = (first := self.initial_sequence[start]) / (second := self.initial_sequence[end])
                new_sequence[f"({first:^8.0f} - {second:^8.0f})"] = ratio
            except ZeroDivisionError:
                new_sequence[f"{first:^8.0f} {second:^8.0f}"] = 0

            start += 1
            end += 1

            if end >= len(self.initial_sequence):
                break

        return new_sequence

    @property
    def ratios_df(self):

        series_values = pd.Series(self.ratios_dict.keys())
        series_ratios = pd.Series(self.ratios_dict.values())
        df = pd.DataFrame({"Numbers": series_values, "Ratio": series_ratios})

        return df

    @property
    def ratios_df_reversed(self):
        
        series_values = pd.Series(self.ratios_dict_reversed.keys())
        series_ratios = pd.Series(self.ratios_dict_reversed.values())
        df = pd.DataFrame({"Numbers": series_values, "Ratio": series_ratios})

        return df