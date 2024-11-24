from fibonacci_sequence_copy import FibonacciSequence, Sequences, Viewer
from tkinter import *
from tkinter import ttk
"""
All these instances are aggregated automatically in Sequences._all_instances
"""


class App(Tk):
    
    def __init__(self, appname):
        super().__init__()
        self.title(appname)
        self.geometry("800x600")
        self.sequence_repr = StringVar(self)

    def __call__(self):
        
        self.load_static_fibonacci_sequences()
        
        self.mybutton = Button(self, text=self.sequence_repr.get())
        self.mybutton.pack()

        self.mainloop()

    def set_static_stringvars(self):
        self.sequence_repr.set(Sequences.get_all()[0].sequence)


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

App("Fibonacci App")()