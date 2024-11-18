from typing import Any

class FibonacciSequence:
    """
        FibonacciSequence is a tool for getting Fibonacci sequence numbers

        ### Example usage:

        ```python

            # This will get 10 fibonacci sequence values including initial values [0, 1]
            new_fibo_sequence = FibonacciSequence([0, 1], 10)

            # Call it for printed output to the terminal in float format
            new_fibo_sequence()

            Terminal output:
                '''
                    1.0000000000
                    2.0000000000
                    3.0000000000
                    5.0000000000
                    8.0000000000
                    13.0000000000
                    21.0000000000
                    34.0000000000
                    55.0000000000
                    89.0000000000
                '''

            # Call it and chain .return_sequence property for the actual sequence

            the_sequence = new_fibo_sequence().return_sequence
        ```
    """
    def __init__(self, initial_items: list = [0, 1], limit: int = 20) -> None:
        
        self.initial_items = initial_items

        try:
            if (initial_values_length := len(initial_items)) > 2:
                raise ValueError("Initial items list must have maximum 2 values to start the sequence with")
            elif initial_values_length < 2:
                raise ValueError("Initial items list must have 2 values to begin the sequence")
        except ValueError:
            print(ValueError)
            values = []
            val1 = input("New first value: ")
            val2 = input("New second value: ")
            
            self.initial_items = []
            self.initial_items.append(float(val1))
            self.initial_items.append(float(val2))

        
        self.sequence_items: list = []
        self.limit: int = limit - len(initial_items)
        
    def __call__(self) -> Any:
        
        values_index = 0
        initial_items = self.initial_items

        # Loop through all items in initial items list
        for item in initial_items:
            # Add these items to sequence list
            self.sequence_items.append(item)

        # For every value in sequence list 
        for _ in self.sequence_items:
            
            # Get the sum of initial numbers and continue moving index to get next ones
            sum = self.sequence_items[(next_value_index := values_index)]\
                  + self.sequence_items[(next_value_index + 1)]
            # Add the sum to the sequence
            self.sequence_items.append(sum)
            
            print(f"{sum:10.3f}")
            if values_index > self.limit:
                break
            values_index += 1

        return self
    @property
    def return_sequence(self) -> list:
        return self.sequence_items

