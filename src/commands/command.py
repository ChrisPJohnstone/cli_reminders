from abc import ABC, abstractmethod
from argparse import _SubParsersAction


class Command(ABC):
    @staticmethod
    @abstractmethod
    def add_args(subparsers: _SubParsersAction) -> None:
        pass
