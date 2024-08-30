from argparse import ArgumentParser, Namespace


if __name__ == "__main__":
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
    print(args)
    print(args.when, type(args.when))
