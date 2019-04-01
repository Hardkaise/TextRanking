#!/usr/bin/env python3

import sys
from src.parsing import error_argument
from src.file import read_file
from src.parser import parse
from src.graphics import graph
from src.parsing import nb_display
from src.parsing import usage
from src.parsing import win_width
from src.parsing import win_height
from src.parsing import is_file_empty
from src.parsing import is_dict_empty
from os.path import splitext, basename

if __name__ == '__main__':
    error_argument(sys.argv.__len__())
    usage(sys.argv[1])
    content = read_file(sys.argv[1])
    nb = nb_display(sys.argv)
    win_x = win_width(sys.argv)
    win_y = win_height(sys.argv)
    is_file_empty(content)
    dict = parse(content)
    is_dict_empty(dict)
    graph(dict, nb, win_x, win_y, basename(splitext(sys.argv[1])[0]))

