# -*- coding: utf-8 -*-
import re


def read_schedule(path: str, mode: str, enc: str) -> str:
    """
    read the input .inc file forming a string of text
    :param path: path to the input .inc file
    :param mode: reading mode
    :param enc: encoding
    :return: string of input text
    """
    return open(path, mode=mode, encoding=enc).read()


def inspect_schedule(text: str) -> bool:
    """
    inspect schedule syntax
    :param text: input text from .inc file
    :return: inspected
    """
    return True


def clean_schedule(text: str) -> str:
    """
    clean '-- ' comments and other
    :param text: inspected input text from .inc file
    :return: cleaned input text from .inc file
    """
    clean_text = re.sub('--.*\n', '\n', text)
    clean_text = re.sub('\s*\n', '\n', clean_text)
    clean_text = re.sub('\n{2,}', '\n', clean_text)
    return clean_text
