from argparse import _SubParsersAction, ArgumentParser, Namespace
from typing import Type

from src.commands import (
    Command,
    Create,
    Send,
)

COMMANDS: dict[str, Type[Command]] = {
    "create": Create,
    "send": Send,
}


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    subparsers: _SubParsersAction = parser.add_subparsers(
        dest="command",
        required=True,
    )
    for command in COMMANDS.values():
        command.add_args(subparsers)
    args: Namespace = parser.parse_args()
    command: Type[Command] = COMMANDS[args.command](args)
    # TODO: Consider moving logic out of init


if __name__ == "__main__":
    main()
