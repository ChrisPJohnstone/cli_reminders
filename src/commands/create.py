from argparse import _SubParsersAction, ArgumentParser

from .command import Command


class Create(Command):
    @staticmethod
    def add_args(subparsers: _SubParsersAction) -> None:
        parser: ArgumentParser = subparsers.add_parser("create")
        parser.add_argument(
            "-d",
            "--date",
            dest="reminder_date",
            metavar="date",
            type=str,
            required=False,
            help="Date reminder should be sent",
        )
        parser.add_argument(
            "-t",
            "--time",
            dest="reminder_time",
            metavar="time",
            type=str,
            required=False,
            help="Time reminder should be sent",
        )
        parser.add_argument(
            dest="message",
            metavar="message",
            nargs="+",
            type=str,
            help="Message reminder should display",
        )
