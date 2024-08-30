from argparse import ArgumentParser, Namespace


VALID_INCREMENTS: list[str] = [
    "something",
    "orother",
]


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        dest="when",
        type=str,
        choices=VALID_INCREMENTS,
        help="Message for reminder",
    )
    parser.add_argument(
        dest="message",
        nargs="*",
        type=str,
        help="Message for reminder",
    )
    args: Namespace = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
