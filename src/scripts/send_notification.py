from argparse import ArgumentParser, Namespace

from src.notification import Client as NotificationClient


def send_notification() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        "--title",
        dest="title",
        metavar="title",
        type=str,
        required=False,
        help="Notification's title",
    )
    parser.add_argument(
        "--application-name",
        dest="application_name",
        metavar="application_name",
        type=str,
        required=False,
        help="Notificiation's application name",
    )
    parser.add_argument(
        "--message",
        dest="message",
        metavar="message",
        type=str,
        required=True,
        help="Notification's message",
    )
    args: Namespace = parser.parse_args()
    notification_client: NotificationClient = NotificationClient(
        title=args.title,
        application_name=args.application_name,
    )
    notification_client.send_notification(args.message)


if __name__ == "__main__":
    send_notification()
