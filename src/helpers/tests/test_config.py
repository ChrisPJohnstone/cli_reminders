from datetime import date, time
from unittest.mock import MagicMock, patch
import pytest

from src.helpers import Config


reminder_date_tests: list[tuple[str | None, date]] = [
    (None, date.today()),
    ("", date.today()),
    ("2024-01-01", date(2024, 1, 1)),
    ("1900-11-11", date(1900, 11, 11)),
]


@patch.object(Config, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], reminder_date_tests)
def test_reminder_date(value: str, expected: str) -> None:
    config: Config = Config("", "", [""])
    config.reminder_date = value
    assert config.reminder_date == expected


reminder_time_tests: list[tuple[str, str]] = [
    ("09", time(9)),
    ("15", time(15)),
    ("23", time(23)),
    ("09:01", time(9, 1)),
    ("09:25", time(9, 25)),
    ("09:52", time(9, 52)),
    ("09:01:02", time(9, 1, 2)),
    ("09:01:11", time(9, 1, 11)),
    ("09:01:42", time(9, 1, 42)),
    ("0901", time(9, 1)),
    ("0925", time(9, 25)),
    ("0952", time(9, 52)),
    ("090102", time(9, 1, 2)),
    ("090111", time(9, 1, 11)),
    ("090142", time(9, 1, 42)),
]


@patch.object(Config, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], reminder_time_tests)
def test_reminder_time(value: str, expected: str) -> None:
    config: Config = Config("", "", [""])
    config.reminder_time = value
    assert config.reminder_time == expected


message_tests: list[tuple[list[str], str]] = [
    (["test"], "test"),
    (["This", "is", "a", "message"], "This is a message"),
]


@patch.object(Config, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], message_tests)
def test_message(value: list[str], expected: str) -> None:
    config: Config = Config("", "", [""])
    config.message = value
    assert config.message == expected
