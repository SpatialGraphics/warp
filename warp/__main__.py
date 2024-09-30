import argparse
import sys
import sysconfig  # type: ignore
import os

def include_dir() -> str:
    "Return the path to the nanobind include directory"
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "native")
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include_dir",
        action="store_true",
        help="Print the path to the nanobind C++ header directory."
    )
    args = parser.parse_args()
    if not sys.argv[1:]:
        parser.print_help()
    if args.include_dir:
        print(include_dir())


if __name__ == "__main__":
    main()
