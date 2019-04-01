def error_argument(arg_size):
    if arg_size <= 3:
        print("Please enter a file in argument when you use this script.")
        exit(84)
    elif arg_size > 5:
        print("Error: Too much arguments.")
        exit(84)


def usage(argv):
    if argv == "--help":
        print("\nUSAGE:\n"
              "\t./indexer.py file nb win_x win_y\n"
              "\t./indexer.py --help\n\n"
              "\t\t--help display help\n"
              "\t\tfile: a .txt filename\n"
              "\t\tnb: number of words display in the graphics (default 25) (optional)\n"
              "\t\twin_x: width in pixel of the window (ex: 1920 pixel -> 19.2) (default = 1920) (optional)\n"
              "\t\twin_y: height in pixel of the window (ex: 1080 pixel -> 10.8) (default = 1080) (optional)\n")
        exit(0)


def is_file_empty(content):
    if content is None or len(content) == 0:
        print("Error: The file is empty.")
        exit(84)


def is_dict_empty(dict):
    if len(dict) == 0:
        print("Error: No words found")
        exit(84)