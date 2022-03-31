import re
from typing import Tuple, List, Any
import numpy as np
import pandas as pd


def transform_schedule(keywords: Tuple[str], parameters: Tuple[str], input_file: str, output_file: str) -> pd.DataFrame:
    """
    read the input .inc-file and transform it to .csv schedule
    your main function
    @param keywords: a tuple of keywords we are interested in (DATES, COMPDAT, COMPDATL, etc.)
    @param parameters: column names of output .csv file
    @param input_file: path to your source input .inc file
    @param output_file: path to your output .csv file
    @return:
    """
    return


def parse_schedule(text: str, keywords_tuple: Tuple[str]) -> List[List[str]]:
    """
    return list of elements ready to be transformed to the resulting DataFrame
    @param text: cleaned input text from .inc file
    @param keywords_tuple: a tuple of keywords we are interested in (DATES, COMPDAT, COMPDATL, etc.)
    @return: list of elements [[DATA1, WELL1, PARAM1, PARAM2, ...], [DATA2, ...], ...] ready to be transformed
    to the resulting DataFrame
    """


# 3 функции ниже можете написать на своё усмотрение, тут они выглядят тяжеловато
def extract_keyword_blocks(text: str, keywords_tuple: Tuple[str]) -> List[Tuple[str]]:
    """
    return keywords text blocks ending with a newline "/"
    @param text: cleaned input text from .inc file
    @param keywords_tuple: a tuple of keywords we are interested in (DATES, COMPDAT, COMPDATL, etc.)
    @return: list keywords text blocks ending with a newline "/"
    """
    list_of_blocks = re.split('\n/\n', text)
    list_of_tuples = [tuple(i.splitlines()) for i in list_of_blocks]
    for tuple_ in list_of_tuples:
        if tuple_[0] not in keywords_tuple:
            list_of_tuples.remove(tuple_)
    return list_of_tuples


def extract_lines_from_keyword_block(block: Tuple[str]) -> Tuple[str, List[str]]:
    """
    extract the main keyword and corresponding lines from a certain block from the input file
    @param block: a block of the input text related to the some keyword (DATA, COMPDAT, etc.)
    @return:
        - keyword - DATA, COMPDAT, etc.
        - lines - lines of the input text related to the current keyword
    """
    return block[0], list(block[1:])


def parse_keyword_block(keyword: str, keyword_lines: List[str], current_date: Any,
                        schedule_list: List[List[str]], block_list: List[List[str]]) \
        -> Tuple[str, List[List[str]], List[List[str]]]:
    """
    parse a block of the input text related to the current keyword (DATA, COMPDAT, etc.)
    @param keyword: DATA, COMPDAT, etc.
    @param keyword_lines: lines of the input text related to the current keyword
    @param current_date: the last parsed DATE. The first DATE is NaN if not specified
    @param schedule_list: list of elements [[DATA1, WELL1, PARAM1, PARAM2, ...], [DATA2, ...], ...]
    @param block_list: schedule_list but for the current keyword
    @return:
        - current_date - current DATE value which might be changed if keyword DATES appears
        - schedule_list - updated schedule_list
        - block_list - updated block_list
    """

    # парсим строки с параметрами, находящиеся в блоке под конкретным кл. словом. просится в отдельный модуль


def parse_keyword_DATE_line(current_date_line: str) -> str:
    """
    parse a line related to a current DATA keyword block
    @param current_date_line: line related to a current DATA keyword block
    @return: list of parameters in a DATE line
    """
    return re.search(r'\d{2} [A-Z]{3} \d{4}', current_date_line).group(0)


def parse_keyword_COMPDAT_line(well_comp_line: str) -> List[str]:
    """
    parse a line related to a current COMPDAT keyword block
    @param well_comp_line: line related to a current COMPDAT keyword block
    @return: list of parameters (+ NaN Loc. grid. parameter) in a COMPDAT line
    """
    well_comp_line = re.sub(r'\'', ' ', well_comp_line)
    well_comp_line = re.sub(r'\s+', ' ', well_comp_line)

    unpacked_well_comp_line = default_params_unpacking_in_line(well_comp_line)
    parameters_list = unpacked_well_comp_line.split()
    parameters_list[1:1] = [np.nan]

    return parameters_list[:-1]


def parse_keyword_COMPDATL_line(well_comp_line: str) -> List[str]:
    """
    parse a line related to a current COMPDATL keyword block
    @param well_comp_line: line related to a current COMPDATL keyword block
    @return: list of parameters in a COMPDATL line
    """
    well_comp_line = re.sub(r'\'', ' ', well_comp_line)
    well_comp_line = re.sub(r'\s+', ' ', well_comp_line)

    unpacked_well_comp_line = default_params_unpacking_in_line(well_comp_line)
    parameters_list = unpacked_well_comp_line.split()

    return parameters_list[:-1]


def default_params_unpacking_in_line(line: str) -> str:
    """
    unpack default parameters set by the 'n*' expression
    @param line: line related to a current COMPDAT/COMPDATL keyword block
    @return: the unpacked line related to a current COMPDAT/COMPDATL keyword block
    """
    unpacked_line = line
    all_asterisks = re.findall(r' \d+\*', unpacked_line)

    for pattern in all_asterisks:
        # change to \* in pattern to use asterisk not as a special symbol
        actual_pattern = pattern[:-1]+'\*'
        unpacked_line = re.sub(actual_pattern, ' DEFAULT' * int(pattern[:-1]), unpacked_line)

    return unpacked_line
