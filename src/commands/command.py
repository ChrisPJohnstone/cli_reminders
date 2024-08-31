from argparse import _SubParsersAction
from abc import ABC, abstractmethod


class Command(ABC):
    @staticmethod
    @abstractmethod
    def add_args(subparsers: _SubParsersAction) -> None:
        pass
