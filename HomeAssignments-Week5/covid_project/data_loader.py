
import pandas as pd

class DataLoader:
    """
    Responsible for loading COVID-19 dataset.
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """
        Loads CSV file into Data Frame.
        """
        df = pd.read_csv(self.filepath)
        pd.DataFrame(df)
        return df
    


    