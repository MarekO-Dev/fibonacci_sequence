from typing import Any
import pandas as pd

class FibonacciSequence:
    
    def __init__(self, 
                 initial_items: list[float] = [float(0), float(1)], 
                 limit: int = 20) -> None:
        
        self.initial_items: list[float] = initial_items
        self.sequence_items: list = []
        self.limit: int = (limit - len(initial_items)) - 1

        try:
            if (initial_values_length := len(initial_items)) > 2:
                raise ValueError("Initial items list must have maximum 2 values to start the sequence with")

            elif initial_values_length < 2:
                raise ValueError("Initial items list must have 2 values to begin the sequence")

        except ValueError:

            val1 = input("New first value: ")
            val2 = input("New second value: ")
            
            self.initial_items = []
            self.initial_items.append(float(val1))
            self.initial_items.append(float(val2))
            self.limit = (limit - len(self.initial_items)) - 1
    
        
    def __call__(self, 
                 printout = False) -> Any:
        
        values_index = 0
        # Loop through all items in initial items list
        for item in self.initial_items:
            # Add these items to sequence list
            self.sequence_items.append(item)

        # For every value in sequence list 
        for _ in self.sequence_items:
            
            # Get the sum of initial numbers and continue moving index to get next ones
            sum = float(self.sequence_items[(next_value_index := values_index)])\
                  + float(self.sequence_items[(next_value_index + 1)])
            # Add the sum to the sequence
            self.sequence_items.append(float(sum))

            if values_index >= self.limit:
                break
            values_index += 1
        
        if printout:

            for val in self.sequence_items:
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

        return self.sequence_items

    @property
    def return_ratios_list(self) -> list:
        
        new_sequence: list = []
        
        start = 0
        end = 1

        for _ in self.sequence_items:
            
            try:
                ratio = self.sequence_items[end] / self.sequence_items[start]
                new_sequence.append(ratio)
            except ZeroDivisionError:
                new_sequence.append(None)

            start += 1
            end += 1

            if end >= len(self.sequence_items):
                break

        return new_sequence
    
    @property
    def return_ratios_dict(self) -> dict:
        
        new_sequence: dict = {}
        
        start = 0
        end = 1

        for _ in self.sequence_items:
            
            try:
                ratio = (second := self.sequence_items[end]) / (first := self.sequence_items[start])
                new_sequence[f"{first:.0f}-{second:.0f}"] = ratio
            except ZeroDivisionError:
                new_sequence[f"{first:.0f}-{second:.0f}"] = 0

            start += 1
            end += 1

            if end >= len(self.sequence_items):
                break

        return new_sequence

    @property
    def return_ratios_dict_reversed(self) -> dict:
        
        new_sequence: dict = {}
        
        start = 0
        end = 1

        for _ in self.sequence_items:
            
            try:
                ratio = (first := self.sequence_items[start]) / (second := self.sequence_items[end])
                new_sequence[f"{first:.0f}-{second:.0f}"] = ratio
            except ZeroDivisionError:
                new_sequence[f"{first:.0f}-{second:.0f}"] = 0

            start += 1
            end += 1

            if end >= len(self.sequence_items):
                break

        return new_sequence

    @property
    def return_ratios_df(self):

        series_values = pd.Series(self.return_ratios_dict.keys())
        series_ratios = pd.Series(self.return_ratios_dict.values())
        df = pd.DataFrame({"Value": series_values, "Ratio": series_ratios})

        return df

    @property
    def return_ratios_df_reversed(self):
        
        series_values = pd.Series(self.return_ratios_dict_reversed.keys())
        series_ratios = pd.Series(self.return_ratios_dict_reversed.values())
        df = pd.DataFrame({"Value": series_values, "Ratio": series_ratios})

        return df