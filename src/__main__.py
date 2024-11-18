from fibonacci_sequence import FibonacciSequence

new_fibonacci_sequence = FibonacciSequence([0], 10)
sequence_list = new_fibonacci_sequence().return_sequence

print("The sequence: ", type(sequence_list))