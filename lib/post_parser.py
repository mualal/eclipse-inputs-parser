import re
from typing import Tuple, List, Union
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def results_to_csv(schedule_list: List[List[str]], csv_file: str, columns: Union[bool, Tuple[str]]) -> pd.DataFrame:
    """
    form PanDas dataframe with results and (optional) writes it into .csv file
    @param schedule_list: list of elements [[DATA1, WELL1, PARAM1, PARAM2, ...], [DATA2, ...], ...]
    @param csv_file: path to .csv file to save PanDas dataframe with results
    @param columns: list of columns in output .csv file
    @return: PanDas dataframe with results
    """


def find_schedule_well_data(schedule_df: pd.DataFrame, well: str, date: str = "ALL_DATES") -> pd.DataFrame:
    """
    find appearances of completions for a certain well and (optional) for a certain date
    @param schedule_df: PanDas dataframe with Well completion schedule
    @param well: certain Well name to find completions
    @param date: certain Date to find completions. Default value is "ALL_DATES"
    @return: PanDas dataframe with a current Well completion schedule
    """
