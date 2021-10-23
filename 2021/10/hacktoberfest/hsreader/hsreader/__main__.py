"""Read the HS3 City Webpage.
Usage:
------
    $ hsreader [options]

Available options are:
    -h, --help         Show this help
    -d, --download     Download HS3 City webpage into chosen directory
    -r, --read         Show HS3 City webpage in terminal

Version:
--------
- hsreader v0.1.0
"""
import sys

import hsreader
from hsreader import download, show

def main():
    """Read HS3City Webpage"""

    # Read url

    url = hsreader.URL
    output_file = hsreader.FILENAME

    # Read options
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    # Perform actions based on the options
    if '-h' in opts or '--help' in opts:
        print(__doc__)
        raise SystemExit()
    elif '-d' in opts or '--download' in opts:
        download(url, output_file)
    elif '-r' in opts or '--read' in opts:
        show(url)
    else:
        print('Option not implement')
        print(__doc__)
        raise SystemExit()


if __name__ == "__main__":
    main()
