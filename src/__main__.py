from fibonacci_sequence_copy import FibonacciSequence, Sequences, Viewer

"""
All these instances are aggregated automatically in Viewer._all_instances
"""

FibonacciSequence(**{
    "starts_with": (0.0, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})

FibonacciSequence(**{
    "starts_with": (0.5, 1),
    "length": 10
})

print(Sequences.count())