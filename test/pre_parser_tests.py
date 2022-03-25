# to run testing use python -m pytest test/pre_parser_tests.py
# use print(repr(str)) to print row str to terminal


import pytest
from lib import pre_parser


def test_clean_schedule():
    assert pre_parser.clean_schedule("COMPDAT\n-- с двух тире начинается комментарий\n'W1' 10 10  1   3 \tOPEN \t1* \t1"
                                     "\t2 \t1 \t3* \t\t\t1.0 /  -- и комментарии могут быть\n'W2' 32 10  1   3 \tOPEN "
                                     "\t1* \t1 \t2 \t1 \t3* \t\t\t2.0 /\n/  -- практически где угодно\n\nCOMPDAT") == \
           "COMPDAT\n'W1' 10 10  1   3 \tOPEN \t1* \t1\t2 \t1 \t3* \t\t\t1.0 /\n'W2' 32 10  1   3 \tOPEN \t1* \t1 " \
           "\t2 \t1 \t3* \t\t\t2.0 /\n/\nCOMPDAT"
