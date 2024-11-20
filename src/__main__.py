from fibonacci_sequence import FibonacciSequence, Viewer

sequence = FibonacciSequence((float(0), float(1)), limit = 12)(printout = False)

print(sequence.ratios_df)
print(sequence.ratios_df_reversed)


Viewer.plot(sequence.ratios_df)