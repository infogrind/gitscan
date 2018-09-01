#!/usr/bin/python

import sys
import getopt
import os
from git import Repo

# Global options with default values.
verbose = False
shownogit = False
showgit = False
showorigin = False


def main():
    args = parse_options(sys.argv[1:])
    debug("Verbose mode enabled.")

    if not (shownogit or showgit or showorigin):
        warn("I won't do anything unless you specify -n, -g, or -o.")

    for d in args:
        processDir(d)


def processDir(d):
    debug("Processing directory %s" % d)
    for sd in listdir_fullpath(d):
        if os.path.isdir(sd):
            debug("Processing subdirectory %s" % sd)
            hasgit = os.path.isdir(os.path.join(sd, ".git"))
            if not hasgit and shownogit:
                print sd
            elif hasgit:
                repo = Repo(sd)
                hasorigin = hasattr(repo.remotes, "origin")
                if hasorigin:
                    if showorigin:
                        print sd 
                elif showgit:
                    print sd


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def usage():
    print """Usage: gitscan <directories>

    Prints git-specific information for each directory given.

    Options:
    -n          Show directories that do not contain a '.git' subdir
    -g          Show directories that DO contain a '.git' subdir but no remote
                named 'origin'.
    -o          Show directories that have an 'origin' remote
    -h          Show this help text.
    -v          Display verbose output.
    """


def parse_options(args):
    
    # Access global variables
    global verbose, shownogit, showgit, showorigin

    # Parse options using Getopt; display an error and exit if options could not
    # be parsed.
    try:
        opts, args = getopt.getopt(args, "ohvngo")
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
        elif opt == "-n":
            shownogit = True
        elif opt == "-g":
            showgit = True
        elif opt == "-o":
            showorigin = True
        else:
            assert False, "unhandled option"

    return args


def debug(s):
    if verbose:
        sys.stderr.write("DEBUG: %s\n" % s)

def warn(s):
    sys.stderr.write("WARN: %s\n" % s)


# This is the most important line: it calls the main function if this program is
# called directly.
if __name__ == "__main__":
    main()

