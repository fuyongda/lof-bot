import sys
import os

here = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(here))
sys.path.insert(0, project_dir)

from lof.examples import render_github


def main():
    render_github("SH501018", "SZ160216")


if __name__ == "__main__":
    main()
