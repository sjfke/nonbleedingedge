import argparse
import sys
import re

# [Date Regex Patterns](https://regexbox.com/regex-templates/date)
DD_MM_YYYY = re.compile(r"^(0[1-9]|[12]\d|3[01]).(0[1-9]|1[0-2]).(19|20)\d{2}$")


def convert_contents(lines, line_numbers=False, verbose=0):
    line_count = 0
    embolden = True

    for line in lines:
        line_count += 1

        if DD_MM_YYYY.match(line.rstrip()):
            # print(f"Date: {line.rstrip()}")
            print(f".. admonition::   {line.rstrip()}")
            print(f"    :collapsible: closed")
        elif line.startswith('https://'):
            print(f"    * `<{line.rstrip()}>`_")
        elif line.startswith('GC:'):
            x = line.rfind('https://')
            if x >= 0:
                print(f"    * related `<{line[x:].rstrip()}>`_")
        elif line != "" and line[0].isalpha():
            if embolden:
                print(f"    **{line.rstrip()}**\n")
                embolden = False
            else:
                print(f"    *{line.rstrip()}*\n")
                embolden = True
        else:
            print(f"    ")
            embolden = True

        if line_numbers:
            print(f"{line_count:03d}: {line.rstrip()}")  # remove newline '\n'

        # else:
        #    print(f"{line.rstrip()}")  # remove newline '\n'

    return None


def display_contents(lines, line_numbers=False, verbose=0):
    line_count = 0

    for line in lines:
        line_count += 1
        if line_numbers:
            print("{:03d}: {}".format(line_count, line.rstrip()))  # remove newline '\n'
        else:
            print("{}".format(line.rstrip()))  # remove newline '\n'

    return None


if __name__ == '__main__':

    arguments = None
    parser = argparse.ArgumentParser(description='Simple version of UNIX cat application')
    parser.add_argument('-c', '--convert', action='store_true', default=False, help='display converted content')
    parser.add_argument('-n', '--number', action='store_true', default=False, help='display line numbers')
    parser.add_argument('-r', '--raw', action='store_true', default=False, help='display raw content')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    args = parser.parse_args()

    if args.verbose > 1:
        print("args: {0}".format(args.__str__()))

    # Note equivalent of: filename = open('filename.txt', 'r')
    # Done by: add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    try:
        contents = args.filename.readlines()

        if args.verbose >= 1:
            print("filename: {0}".format(args.filename))

        if args.raw:
            print("contents: {0}".format(contents))
            sys.exit(0)

        if args.convert:
            convert_contents(lines=contents, line_numbers=args.number, verbose=args.verbose)
        else:
            display_contents(lines=contents, line_numbers=args.number, verbose=args.verbose)

        sys.exit(0)

    except FileNotFoundError as file_not_found_error:
        print("{0}".format(file_not_found_error))
        sys.exit(1)
    except Exception as error:
        print('{0}'.format(error))
        sys.exit(1)