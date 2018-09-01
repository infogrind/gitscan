#!/usr/bin/python

import sys
import getopt

# Global options with default values.
verbose = False
output = "-"


def main():
    args = parse_options(sys.argv[1:])

    print "Output: ", output
    debug("If you see this, verbose mode is enabled.")

    # Complete the program here. Enjoy!


def usage():
    print """Usage: <syntax goes here>

    <description goes here>

    Options:
    -h          Show this help text.
    -v          Display verbose output.
    -o <file> Write output to <file> or to stdout if <file> is '-'.
    """


def parse_options(args):
    
    # Access global variables
    global verbose, output

    # Parse options using Getopt; display an error and exit if options could not
    # be parsed.
    try:
        opts, args = getopt.getopt(args, "o:hv")
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    # Set variables according to options
    for opt, val in opts:
        if opt == "-h":
            usage()
            sys.exit()

        elif opt == "-v":
            verbose = True

        elif opt == "-o":
            output = val
        else:
            assert False, "unhandled option"

    return args


def debug(s):
    if verbose:
        sys.stderr.write(s + "\n")


# This is the most important line: it calls the main function if this program is
# called directly.
if __name__ == "__main__":
    main()

