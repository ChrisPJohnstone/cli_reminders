from argparse import _SubParsersAction, ArgumentParser, Namespace

from .command import Command
from src.schedule import Client as ScheduleClient

COMMAND: str = "create"


class Create(Command):
    def __init__(self, args: Namespace) -> None:
        schedule_client: ScheduleClient = ScheduleClient(
            reminder_date=args.reminder_date,
            reminder_time=args.reminder_time,
            message=args.message,
        )
        schedule_client.write()

    @staticmethod
    def add_args(subparsers: _SubParsersAction) -> None:
        parser: ArgumentParser = subparsers.add_parser(COMMAND)
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
