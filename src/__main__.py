from fibonacci_sequence import FibonacciSequence


new_fibonacci_sequence = FibonacciSequence([float(1), float(2)], 180)
sequence = new_fibonacci_sequence(printout=False)

print(sequence.return_ratios_df)