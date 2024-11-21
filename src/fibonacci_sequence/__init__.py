from typing import Any
import pandas as pd
import matplotlib.pyplot as plt

class Viewer:

    _all_instances: list = []

    def __init__(self, ax) -> None:
        self.ax = ax
        self.current_ylim = 0;

    @classmethod
    def plot(cls, *, ylim: tuple | None = None):

        
        color_list = ["g", "r", "b", "b", "g", "r", "b", "g", "g", "r"\
                        ,"g", "r", "b", "b", "g", "r", "b", "g", "g", "r"\
                            , "r", "b", "b", "g", "r", "b", "g", "g", "r"]
        color_index = 0

        fig, ax = plt.subplots(nrows = 2, ncols = 1)
        fig.canvas.manager.set_window_title("Title")

        ax[0].set_yticks([0.382, 0.5, 0.618, 0.786, 1.618])
        ax[0].set_xticks(cls._all_instances[0].ratios_df.index)

        x = 0.0
        for instance in cls._all_instances:

            instance_df = instance.ratios_df
            instance_rows = instance_df.shape[0]
            instance_cols = instance_df.shape[1]
            
            ax[0].plot(instance_df["Ratio"], f"{color_list[color_index]}.-", mec="#f001", ms=5, linewidth=0.5)

            y = 0.0
            for num in instance_df[["Number1", "Number2"]]:
                for other_val in instance_df[num]:
                    print("OW", other_val)

                ax[1].text(x, 0.7 + y, f"Number: {num}")

                #print("Num: ", num)
                y -= 0.1
            x+= 0.3
            color_index -= 1
        
        ax[0].hlines([1.618033], [-1], [instance_rows], colors="#f00", linestyles="dotted", label="1.618033")
        ax[0].hlines([0.618033], [-1], [instance_rows], colors="#f00", linestyles="dotted", label="0.618033")
        
        ax[0].set_xlabel("Sequence Index")
        ax[0].set_ylabel("Ratio")
        ax[0].legend()

        
        ax[1].set_xticklabels([])
        ax[1].set_yticklabels([])
        ax[1].set_frame_on(False)
        ax[1].set_yticks([])
        ax[1].set_xticks([])
        plt.show()

        

class FibonacciSequence:
    def __init__(self,
                 initial_sequence: tuple[float, float] = (float(0), float(1)),
                 *,
                 limit: int = 20) -> None:
        
        self.initial_sequence: list = list(initial_sequence)
        self.limit: int = (limit - len(self.initial_sequence)) - 1
        Viewer._all_instances.append(self)

    def __call__(self, 
                 printout = False) -> Any:

        values_index = 0

        # For every value in sequence list 
        for _ in self.initial_sequence:
            
            # Get the sum of initial numbers and continue moving index to get next ones
            sum = float(self.initial_sequence[(values_index)])\
                  + float(self.initial_sequence[(values_index + 1)])
            
            # Add the sum to the sequence
            self.initial_sequence.append(float(sum))

            if values_index >= self.limit:
                break

            values_index += 1
        
        if printout:

            for val in self.initial_sequence:
                print(f"{float(val):.^20.4f}")

        return self

    def ratios_dict(self, *, reversed: bool = False) -> dict:
        
        _new_sequence: dict = {
            "Number1": [],
            "Number2": [],
            "Ratio": []
        }
        
        _start: int = 0
        _end: int = 1

        for _ in self.initial_sequence:
            
            try:
                
                if not reversed:

                    ratio = (second := self.initial_sequence[_end]) / (first := self.initial_sequence[_start])
                else:
                    ratio = (second := self.initial_sequence[_start]) / (first := self.initial_sequence[_end])
                
                _new_sequence["Number1"].append(first)
                _new_sequence["Number2"].append(second)
                _new_sequence["Ratio"].append(ratio)
                
            except ZeroDivisionError:

                _new_sequence["Number1"].append(first)
                _new_sequence["Number2"].append(second)
                _new_sequence["Ratio"].append(0)

            _start += 1
            _end += 1

            if _end >= len(self.initial_sequence):
                break

        return _new_sequence
    
    def _get_dict(self, reversed = False):

        ratios_dict = self.ratios_dict(reversed = reversed)

        series_numbers1 = pd.Series(ratios_dict["Number1"])
        series_numbers2 = pd.Series(ratios_dict["Number2"])
        series_ratios = pd.Series(ratios_dict["Ratio"])
        
        return pd.DataFrame({"Number1": series_numbers1, "Number2": series_numbers2, "Ratio": series_ratios})

    @property
    def ratios_df(self):

        return self._get_dict()

    @property
    def ratios_df_reversed(self):
        
        return self._get_dict(reversed = True)