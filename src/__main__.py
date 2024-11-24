from fibonacci_sequence_copy import FibonacciSequence, Sequences, Viewer
from tkinter import *
from tkinter import ttk, font as tkFont



class App(Tk):
    def __init__(self, appname):
        super().__init__()
        self.title(appname)
        self.geometry("800x600")
        self.sequence_repr = StringVar(self)

    def __call__(self):
        helv20 = tkFont.Font(family='Helvetica', size=20, weight='bold')
        initial_screen_elements = {
            "label_for_starts_with_first": Label,
            "label_for_starts_with_second": Label,
            "entry_for_starts_with_first": Entry,
            "entry_for_starts_with_second": Entry,
            "generate_new_sequence_button": Button,
            "view_sequences_button": Button
        }
        
        def generate_labels():

            initial_screen_elements["label_for_starts_with_first"]\
                (self, text="Starts with: (First)").grid(row = 0, column = 0)
            initial_screen_elements["label_for_starts_with_second"]\
                (self, text="Starts with: (Second)").grid(row = 1, column = 0)
            
        def generate_entry_fields():

            initial_screen_elements["entry_for_starts_with_first"]\
                (self, width = 5).grid(row = 0, column = 1) # needs IntVar
            initial_screen_elements["entry_for_starts_with_first"]\
                (self).grid(row = 1, column = 1) # needs IntVar
            
        def generate_buttons():

            initial_screen_elements["generate_new_sequence_button"]\
                (self, text = "Generate new Sequence", cnf={
                    "bg": "#9e8888"
                })\
                    .grid(row = 2, column = 0, columnspan=2)
            initial_screen_elements["view_sequences_button"]\
                (self, text = "View", cnf={
                    "bg": "#0f0",
                    "padx": 30,
                    "pady": 30,
                })\
                    .grid(row = 0, column = 2, rowspan=3)

        def set_elements_fonts():
            aggregated_elements = self.winfo_children()
            for element in aggregated_elements:
                element.configure(font = helv20)

        def start_initial_screen():
            generate_labels()
            generate_entry_fields()
            generate_buttons()

            #below must come after
            set_elements_fonts()
            
        # Init 
        start_initial_screen()
        self.mainloop()


"""
All these instances are aggregated automatically in Sequences._all_instances
"""
'''
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
'''
App("Fibonacci App")() # starts the gui program
