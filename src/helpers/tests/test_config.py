from datetime import date, time
from unittest.mock import _Call, call, MagicMock, patch, PropertyMock
import pytest

from src.helpers import Config


init_args: list[str] = [
    "reminder_date",
    "reminder_time",
    "message",
    "expected_reminder_date_calls",
    "expected_reminder_time_calls",
    "expected_message_calls",
]
init_tests: list[
    tuple[
        str | None,
        str | None,
        list[str],
        list[_Call],
        list[_Call],
        list[_Call],
    ]
] = [
    (None, None, [""], [call(None)], [call(None)], [call([""])]),
    (
        "apple",
        "banana",
        ["cherry", "strawberry"],
        [call("apple")],
        [call("banana")],
        [call(["cherry", "strawberry"])],
    ),
]


@patch.object(Config, "message", new_callable=PropertyMock)
@patch.object(Config, "reminder_time", new_callable=PropertyMock)
@patch.object(Config, "reminder_date", new_callable=PropertyMock)
@pytest.mark.parametrize(init_args, init_tests)
def test_init(
    mock_reminder_date: PropertyMock,
    mock_reminder_time: PropertyMock,
    mock_message: PropertyMock,
    reminder_date: str | None,
    reminder_time: str | None,
    message: list[str],
    expected_reminder_date_calls: list[_Call],
    expected_reminder_time_calls: list[_Call],
    expected_message_calls: list[_Call],
) -> None:
    Config(reminder_date, reminder_time, message)
    mock_reminder_date.assert_has_calls(expected_reminder_date_calls)
    mock_reminder_time.assert_has_calls(expected_reminder_time_calls)
    mock_message.assert_has_calls(expected_message_calls)


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


reminder_date_error_tests: list[tuple[str | None, str]] = [
    ("test", "Reminder date test is not supported"),
]


@patch.object(Config, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], reminder_date_error_tests)
def test_reminder_date_error(value: str, expected: str) -> None:
    config: Config = Config("", "", [""])
    with pytest.raises(NotImplementedError, match=expected):
        config.reminder_date = value


reminder_time_tests: list[tuple[str | None, time]] = [
    (None, time(9)),
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
def test_reminder_time(value: str | None, expected: str) -> None:
    config: Config = Config("", "", [""])
    config.reminder_time = value
    assert config.reminder_time == expected


reminder_time_error_tests: list[tuple[str, str]] = [
    ("test", "Reminder time test is not supported"),
]


@patch.object(Config, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], reminder_time_error_tests)
def test_reminder_time_error(value: str, expected: str) -> None:
    config: Config = Config("", "", [""])
    with pytest.raises(NotImplementedError, match=expected):
        config.reminder_time = value


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
