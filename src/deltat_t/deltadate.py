from typing import Tuple

from .lib import civil_from_days, days_from_civil, last_day_of_month


class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    def __repr__(self):
        return str(self)

    def __eq__(self, __value: object) -> bool:
        return (
            self.hour == __value.hour
            and self.minute == __value.minute
            and self.second == __value.second
        )

    def __ne__(self, __value: object) -> bool:
        return (
            self.hour != __value.hour
            or self.minute != __value.minute
            or self.second != __value.second
        )

    def __lt__(self, __value: object) -> bool:
        return (
            self.hour < __value.hour
            or self.minute < __value.minute
            or self.second < __value.second
        )

    def __le__(self, __value: object) -> bool:
        return (
            self.hour <= __value.hour
            and self.minute <= __value.minute
            and self.second <= __value.second
        )

    def __gt__(self, __value: object) -> bool:
        return (
            self.hour > __value.hour
            or self.minute > __value.minute
            or self.second > __value.second
        )

    def __ge__(self, __value: object) -> bool:
        return (
            self.hour >= __value.hour
            and self.minute >= __value.minute
            and self.second >= __value.second
        )

    def increment(self, seconds):
        self.second += seconds
        if self.second >= 60:
            self.second = 0
            self.minute += 1

        if self.minute >= 60:
            self.minute = 0
            self.hour += 1

        if self.hour >= 24:
            self.hour = 0

    def to_eod(self) -> Tuple[int, int, int]:
        seconds = 60 - self.second
        minutes = 60 - self.minute
        hours = 24 - self.hour


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.nb_days = days_from_civil(year, month, day)

    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        return self.nb_days - other.nb_days

    def __eq__(self, __value: object) -> bool:
        return self.nb_days == __value.nb_days

    def __ne__(self, __value: object) -> bool:
        return self.nb_days != __value.nb_days

    def __lt__(self, __value: object) -> bool:
        return self.nb_days < __value.nb_days

    def __le__(self, __value: object) -> bool:
        return self.nb_days <= __value.nb_days

    def __gt__(self, __value: object) -> bool:
        return self.nb_days > __value.nb_days

    def __ge__(self, __value: object) -> bool:
        return self.nb_days >= __value.nb_days

    def increment(self, days):
        self.nb_days += days
        self.year, self.month, self.day = civil_from_days(self.nb_days)


class DDate(object):
    def __init__(self, d1, d2) -> None:
        self.d1 = d1
        self.d2 = d2

    def diff(self) -> Tuple[int, int, int]:
        if self.d2.nb_days > self.d1.nb_days:
            dh = self.d2
            dl = self.d1
        else:
            dh = self.d1
            dl = self.d2

        days, month, years = 0, 0, 0

        dtp = Date(dl.year, dl.month, dl.day)
        while dtp < dh:
            days += 1
            if days >= last_day_of_month(dtp.year, dtp.month):
                days = 0
                month += 1

            if month >= 12:
                month = 0
                years += 1

            dtp.increment(1)

        return years, month, days

    def __repr__(self) -> str:
        years, months, days = self.diff()
        return f"{years} years, {months} months, {days} days"


class DTime:
    def __init__(self, t1: Time, t2: Time) -> None:
        self.t1 = t1
        self.t2 = t2

    def diff(self) -> Tuple[int, int, int]:
        if self.t2 < self.t1:
            t1 = self.t2
            t2 = self.t1
        else:
            t1 = self.t1
            t2 = self.t2

        hours, minutes, seconds = 0, 0, 0

        while t1 < t2:
            seconds += 1
            if seconds >= 60:
                seconds = 0
                minutes += 1

            if minutes >= 60:
                minutes = 0
                hours += 1

            t1.increment(1)

        return hours, minutes, seconds
