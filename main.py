from lib import pre_parser
import os


if __name__ == '__main__':

    text = pre_parser.read_schedule(os.path.join('input', 'test_schedule.inc'), 'r', 'UTF-8')

    if pre_parser.inspect_schedule(text):
        text = pre_parser.clean_schedule(text)
    else:
        print('Not expected input file')

    with open(os.path.join('output', 'output.inc'), 'w') as f:
        f.write(text)
