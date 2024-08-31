from re import fullmatch


class Config:
    def __init__(self, date: str | None, time: str, message: list[str]) -> None:
        self.date = date
        self.time = time
        self.message = message

    @property
    def time(self) -> str:
        return self._time
        # TODO: Change time property to time type

    @time.setter
    def time(self, time: str) -> None:
        if fullmatch(r"\d{2}(:\d{2}){0,2}", time):
            self._time: str = f"{time}:00:00"[:8]
            return
            # TODO: Find a cleaner solution to this return
        raise NotImplementedError(f"Reminder time {time} is not supported")
