from abc import ABC, abstractmethod
from argparse import _SubParsersAction, Namespace


class Command(ABC):
    @abstractmethod
    def __init__(self, args: Namespace) -> None:
        pass

    @staticmethod
    @abstractmethod
    def add_args(subparsers: _SubParsersAction) -> None:
        pass
