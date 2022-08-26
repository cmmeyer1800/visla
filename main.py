import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import argparse
from src.parser import Parsed
from src.interp import Interpreter


# -----------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help=".vsla source file to run", type=str)

    args = parser.parse_args()

    parsed = Parsed(args.file)

    interpreter = Interpreter(parsed.ast)

    interpreter.run()

    return 0


if __name__ == "__main__":
    exit(main())
