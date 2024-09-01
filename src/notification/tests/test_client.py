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


send_args: list[str] = [
    "title",
    "application_name",
    "message",
    "expected_notify_calls",
]
send_tests: list[tuple[str, str, str, list[_Call]]] = [
    (
        "apple",
        "grape",
        "banana",
        [
            call(
                default_notification_title="apple",
                default_notification_message="banana",
                default_notification_application_name="grape",
            )
        ],
    ),
    (
        "berry",
        "cherry",
        "dairy",
        [
            call(
                default_notification_title="berry",
                default_notification_message="dairy",
                default_notification_application_name="cherry",
            )
        ],
    ),
]


@patch("notification.client.Notify")
@patch.object(Client, "application_name", new_callable=PropertyMock)
@patch.object(Client, "title", new_callable=PropertyMock)
@patch.object(Client, "__init__", new=MagicMock(return_value=None))
@pytest.mark.parametrize(send_args, send_tests)
def test_send(
    mock_title: PropertyMock,
    mock_application_name: PropertyMock,
    mock_notify: MagicMock,
    title: str,
    application_name: str,
    message: str,
    expected_notify_calls: list[_Call],
) -> None:
    mock_title.return_value = title
    mock_application_name.return_value = application_name
    client: Client = Client()
    client.send(message)
    mock_notify.assert_has_calls(expected_notify_calls)
    mock_notify().send.assert_called_once()
