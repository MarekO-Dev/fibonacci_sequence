from fibonacci_sequence import FibonacciSequence, Viewer

sequence = FibonacciSequence((float(1), float(2)), limit = 12)(printout = False)
sequence2 = FibonacciSequence((float(2), float(3)), limit = 12)(printout = False)

#print(sequence.ratios_df)
#print(sequence.ratios_df_reversed)


Viewer.plot([sequence.ratios_df, sequence2.ratios_df])