from lib import parser
import os


if __name__ == '__main__':

    input_file_path = os.path.join('input', 'test_schedule.inc')
    output_file_path = os.path.join('output', 'schedule_output.csv')

    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
                  "Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
                  "Skin factor","Skin factor","Skin factor", "D-factor")

    result = parser.transform_schedule(keywords, parameters, input_file_path, output_file_path)
    print(result)
