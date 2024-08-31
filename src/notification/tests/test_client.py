from unittest.mock import _Call, call, MagicMock, patch, PropertyMock
import pytest

from notification import Client


init_args: list[str] = [
    "title",
    "application_name",
    "expected_title_calls",
    "expected_application_name_calls",
]
init_tests: list[tuple[str | None, str | None, list[_Call], list[_Call]]] = [
    (None, None, [call(None)], [call(None)]),
    ("apple", "grape", [call("apple")], [call("grape")]),
]


@patch.object(Client, "application_name", new_callable=PropertyMock)
@patch.object(Client, "title", new_callable=PropertyMock)
@pytest.mark.parametrize(init_args, init_tests)
def test_init(
    mock_title: PropertyMock,
    mock_application_name: PropertyMock,
    title: str | None,
    application_name: str | None,
    expected_title_calls: list[_Call],
    expected_application_name_calls: list[_Call],
) -> None:
    Client(title, application_name)
    mock_title.assert_has_calls(expected_title_calls)
    mock_application_name.assert_has_calls(expected_application_name_calls)


title_tests: list[tuple[str | None, str]] = [
    (None, "REMINDER"),
    ("test", "test"),
]


@patch.object(Client, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], title_tests)
def test_title(value: str | None, expected: str) -> None:
    client: Client = Client()
    client.title = value
    assert client.title == expected


application_name_tests: list[tuple[str | None, str]] = [
    (None, "REMINDER"),
    ("test", "test"),
]


@patch.object(Client, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(["value", "expected"], application_name_tests)
def test_application_name(value: str | None, expected: str) -> None:
    client: Client = Client()
    client.application_name = value
    assert client.application_name == expected
