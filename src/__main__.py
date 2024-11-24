from fibonacci_sequence_copy import FibonacciSequence, Sequences
from tkinter import *
from tkinter import ttk, font as tkFont

class Viewer(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

    @classmethod
    def start(cls):
        cls().mainloop()
        

class App(Tk):
    def __init__(self, appname):
        super().__init__()
        self.title(appname)
        self.geometry("800x600")
        self.sequence_repr = StringVar(self)

    def __call__(self):
        global_fonts = {
            "helv14": tkFont.Font(family='Helvetica', size=14, weight='normal'),
            "helv18": tkFont.Font(family='Helvetica', size=18, weight='normal')
        }

        initial_screen_elements = {
            "label_for_starts_with_first": Label,
            "label_for_starts_with_second": Label,
            "entry_for_starts_with_first": Entry,
            "entry_for_starts_with_second": Entry,
            "generate_new_sequence_button": Button,
            "view_sequences_button": Button
        }
        
        def display_labels(wrapper):

            initial_screen_elements["label_for_starts_with_first"]\
                (wrapper, text="Starts with: (First)").grid(row = 0, column = 0)
            initial_screen_elements["label_for_starts_with_second"]\
                (wrapper, text="Starts with: (Second)").grid(row = 1, column = 0)
            
        def display_entry_fields(wrapper):
            
            global_font_options = {
                "master": wrapper,
                "width": 5
            }

            initial_screen_elements["entry_for_starts_with_first"]\
                (**global_font_options).grid(row = 0, column = 1) # needs IntVar
            initial_screen_elements["entry_for_starts_with_first"]\
                (**global_font_options).grid(row = 1, column = 1) # needs IntVar
            
        def display_buttons(wrapper):
            
            global_button_options = {
                "master": wrapper
            }

            initial_screen_elements["generate_new_sequence_button"]\
                (**global_button_options, text = "Generate new Sequence", cnf={
                    "bg": "#9e8888"
                })\
                    .grid(row = 2, column = 0, columnspan=2)
            
            initial_screen_elements["view_sequences_button"]\
                (**global_button_options, text = "View", cnf={
                    "bg": "#0f0",
                    "padx": 30,
                    "pady": 30,
                }, command=lambda: Viewer.start())\
                    .grid(row = 0, column = 2, rowspan=3)

        def set_elements_fonts(wrapper):
            aggregated_elements = wrapper.winfo_children()
            for element in aggregated_elements:
                element.configure(font = global_fonts["helv14"])

        def start_initial_screen():
            """
            Init function for the main screen

            1. It creates a wrapper for the elements
            2. Displays elements on screen
            
            """
            wrapper = Frame(self)
            wrapper.pack(expand = True)

            display_labels(wrapper)
            display_entry_fields(wrapper)
            display_buttons(wrapper)

            #below must come after
            set_elements_fonts(wrapper)
            
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
