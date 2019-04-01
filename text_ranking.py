#!/usr/bin/env python3

import sys

from src.file import read_file
from src.parser import parse
from src.parsing import error_argument
from src.parsing import is_dict_empty
from src.parsing import is_file_empty
from src.parsing import usage
from src.vector_space_model import cosine_calculation

if __name__ == '__main__':
    error_argument(len(sys.argv))
    usage(sys.argv[1])
    content1 = read_file(sys.argv[1])
    content2 = read_file(sys.argv[2])
    is_file_empty(content1)
    is_file_empty(content2)
    dict1 = parse(content1)
    dict2 = parse(content2)
    is_dict_empty(dict1)
    is_dict_empty(dict2)
    query = dict()
    query[sys.argv[3]] = 1
    cosine_calculation(dict1, dict2, query, sys.argv[3], sys.argv[1], sys.argv[2])

