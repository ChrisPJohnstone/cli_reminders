from argparse import ArgumentParser, Namespace

from .helpers import Config


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        dest="--date",
        metavar="date",
        type=str,
        required=False,
        help="Date reminder should be sent",
    )
    parser.add_argument(
        dest="time",
        metavar="time",
        type=str,
        help="Time reminder should be sent",
    )
    parser.add_argument(
        dest="message",
        metavar="message",
        nargs="*",
        type=str,
        help="Message reminder should display",
    )
    args: Namespace = parser.parse_args()
    config: Config = Config(**vars(args))
    print(config)


if __name__ == "__main__":
    main()
