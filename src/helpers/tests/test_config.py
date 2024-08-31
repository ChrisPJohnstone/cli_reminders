from datetime import date, time
from unittest.mock import MagicMock, patch
import pytest

from helpers import Config


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
    ("09", "09:00:00"),
    ("15", "15:00:00"),
    ("23", "23:00:00"),
    ("09:01", "09:01:00"),
    ("09:25", "09:25:00"),
    ("09:52", "09:52:00"),
    ("09:01:02", "09:01:02"),
    ("09:01:11", "09:01:11"),
    ("09:01:42", "09:01:42"),
]


@patch.object(Config, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], reminder_time_tests)
def test_reminder_time(value: str, expected: str) -> None:
    config: Config = Config("", "", [""])
    config.reminder_time = value
    assert config.reminder_time == expected
