from unittest.mock import MagicMock, patch
import pytest

from helpers import Config


time_tests: list[tuple[str, str]] = [
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
@pytest.mark.parametrize(["value", "expected"], time_tests)
def test_time(value: str, expected: str) -> None:
    config: Config = Config("", "", [""])
    config.time = value
    assert config.time == expected
