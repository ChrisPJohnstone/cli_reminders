from argparse import Namespace
from datetime import date, datetime, time
from re import fullmatch


class Client:
    def __init__(self, args: Namespace) -> None:
        self.reminder_date = args.reminder_date
        self.reminder_time = args.reminder_time
        self.message = args.message

    @property
    def DEFAULT_REMINDER_DATE(self) -> date:
        return date.today()

    @property
    def reminder_date(self) -> date:
        return self._reminder_date

    @reminder_date.setter
    def reminder_date(self, value: str | None) -> None:
        if not value:
            self._reminder_date: date = self.DEFAULT_REMINDER_DATE
        elif fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            parsed: datetime = datetime.strptime(value, "%Y-%m-%d")
            self._reminder_date: date = parsed.date()
        else:
            raise NotImplementedError(f"Reminder date {value} is not supported")

    @property
    def DEFAULT_REMINDER_TIME(self) -> time:
        return time(9)

    @property
    def reminder_time(self) -> time:
        return self._reminder_time

    @reminder_time.setter
    def reminder_time(self, value: str | None) -> None:
        if not value:
            self._reminder_time: time = self.DEFAULT_REMINDER_TIME
        elif fullmatch(r"\d{2}(:?\d{2}){0,2}", value):
            cleaned: str = f"{value.replace(':', '')}0000"[:6]
            self._reminder_time: time = time(
                hour=int(cleaned[:2]),
                minute=int(cleaned[2:4]),
                second=int(cleaned[4:]),
            )
        else:
            raise NotImplementedError(f"Reminder time {value} is not supported")

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, value: list[str]) -> None:
        self._message: str = " ".join(value)
