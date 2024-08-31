from re import fullmatch
from datetime import date, datetime, time


class Config:
    def __init__(
        self,
        reminder_date: str | None,
        reminder_time: str,
        message: list[str],
    ) -> None:
        self.reminder_date = reminder_date
        self.reminder_time = reminder_time
        self.message = message

    @property
    def DEFAULT_DATE(self) -> date:
        return date.today()

    @property
    def reminder_date(self) -> date:
        return self._reminder_date

    @reminder_date.setter
    def reminder_date(self, value: str | None) -> None:
        if not value:
            self._reminder_date: date = self.DEFAULT_DATE
            return
        elif fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            parsed: datetime = datetime.strptime(value, "%Y-%m-%d")
            self._reminder_date: date = parsed.date()
            return
        # TODO: Find a cleaner solution than return
        raise NotImplementedError(f"Reminder date {value} is not supported")

    @property
    def reminder_time(self) -> str:
        return self._time
        # TODO: Change time property to time type

    @reminder_time.setter
    def reminder_time(self, value: str) -> None:
        if fullmatch(r"\d{2}(:\d{2}){0,2}", value):
            self._time: str = f"{value}:00:00"[:8]
            return
        # TODO: Find a cleaner solution than return
        raise NotImplementedError(f"Reminder time {value} is not supported")
