from fibonacci_sequence import FibonacciSequence

sequence = FibonacciSequence((float(0), float(1)), limit = 10)(printout = False)

print(sequence.ratios_df)
print(sequence.ratios_df_reversed)