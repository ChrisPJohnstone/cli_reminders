from argparse import ArgumentParser, Namespace

from .helpers import Config
from .notification import Client as NotificationClient


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--date",
        dest="reminder_date",
        metavar="date",
        type=str,
        required=False,
        help="Date reminder should be sent",
    )
    parser.add_argument(
        "-t",
        "--time",
        dest="reminder_time",
        metavar="time",
        type=str,
        required=False,
        help="Time reminder should be sent",
    )
    parser.add_argument(
        dest="message",
        metavar="message",
        nargs="*",
        type=str,
        help="Message reminder should display",
    )
    args: Namespace = parser.parse_args()
    config: Config = Config(**vars(args))
    notification_client: NotificationClient = NotificationClient()
    notification_client.send_notification(config.message)


if __name__ == "__main__":
    main()
