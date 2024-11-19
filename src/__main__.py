from fibonacci_sequence import FibonacciSequence

new_fibonacci_sequence = FibonacciSequence([float(1), float(2)], 20)
sequence = new_fibonacci_sequence(printout=True)

sequence_list = sequence.return_sequence
sequence_ratios_list = sequence.return_ratios_list
sequence_ratios_dict = sequence.return_ratios_dict
print("SL:", sequence_list)
print("SRL:", sequence_ratios_list)
print("SRD:", sequence_ratios_dict)

sequence.printout_sequence_ratio()