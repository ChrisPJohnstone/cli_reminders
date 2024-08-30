from argparse import ArgumentParser, Namespace
from sys import stdout


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        dest="when",
        type=str,
        help="When to send reminder",
    )
    parser.add_argument(
        dest="message",
        type=str,
        help="Message for reminder",
    )
    args: Namespace = parser.parse_args()
    stdout.write(args.when)


if __name__ == "__main__":
    main()
