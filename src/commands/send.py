from argparse import _SubParsersAction, ArgumentParser

from .command import Command

COMMAND: str = "send"


class Send(Command):
    @staticmethod
    def add_args(subparsers: _SubParsersAction) -> None:
        parser: ArgumentParser = subparsers.add_parser(COMMAND)
        parser.add_argument(
            "--title",
            dest="title",
            metavar="title",
            type=str,
            required=False,
            help="Notification's title",
        )
        parser.add_argument(
            "--application-name",
            dest="application_name",
            metavar="application_name",
            type=str,
            required=False,
            help="Notificiation's application name",
        )
        parser.add_argument(
            "--message",
            dest="message",
            metavar="message",
            type=str,
            required=True,
            help="Notification's message",
        )
