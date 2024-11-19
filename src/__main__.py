from fibonacci_sequence import FibonacciSequence

new_fibonacci_sequence = FibonacciSequence((float(0), float(1)), limit = 10)
sequence = new_fibonacci_sequence(printout=False)

print(sequence.ratios_df)
print(sequence.ratios_df_reversed)