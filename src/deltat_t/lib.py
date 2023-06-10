# Implementation of Algorithm explained by Howard Hinnant in https://howardhinnant.github.io/date_algorithms.html
# The Goal is to test Naive timedelta implementation

from typing import Tuple

DAYS_OF_MONTH = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
]

DAYS_OF_MONTH_LEAP_YEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_from_civil(y: int, m: int, d: int) -> int:
    # y -= m <= 2;
    y -= 1 if m <= 2 else 0
    # const Int era = (y >= 0 ? y : y-399) / 400;
    era = y // 400 if y >= 0 else (y - 399) // 400
    # const unsigned yoe = static_cast<unsigned>(y - era * 400);      // [0, 399]
    yoe = y - era * 400
    # const unsigned doy = (153*(m > 2 ? m-3 : m+9) + 2)/5 + d-1;  // [0, 365]
    doy = (153 * (m - 3 if m > 2 else m + 9) + 2) // 5 + d - 1
    # const unsigned doe = yoe * 365 + yoe/4 - yoe/100 + doy;         // [0, 146096]
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy

    # return era * 146097 + static_cast<Int>(doe) - 719468;
    return era * 146097 + doe - 719468


def civil_from_days(z: int) -> Tuple[int, int, int]:
    z += 719468
    # era = (z >= 0 ? z : z - 146096) / 146097;
    era = (z if z >= 0 else z - 146096) // 146097
    # const unsigned doe = static_cast<unsigned>(z - era * 146097);          // [0, 146096]
    doe = z - era * 146097
    # const unsigned yoe = (doe - doe/1460 + doe/36524 - doe/146096) / 365;  // [0, 399]
    yoe = (doe - doe // 1460 + doe // 36524 - doe // 146096) // 365
    # const Int y = static_cast<Int>(yoe) + era * 400;
    y = yoe + era * 400
    # const unsigned doy = doe - (365*yoe + yoe/4 - yoe/100);                // [0, 365]
    doy = doe - (365 * yoe + yoe // 4 - yoe // 100)
    # const unsigned mp = (5*doy + 2)/153;                                   // [0, 11]
    mp = (5 * doy + 2) // 153
    # const unsigned d = doy - (153*mp+2)/5 + 1;                             // [1, 31]
    d = doy - (153 * mp + 2) // 5 + 1
    # const unsigned m = mp < 10 ? mp+3 : mp-9;                            // [1, 12]
    m = mp + 3 if mp < 10 else mp - 9

    # return std::tuple<Int, unsigned, unsigned>(y + (m <= 2), m, d);
    return y + (m <= 2), m, d


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def last_day_of_month_common_year(month: int) -> int:
    return DAYS_OF_MONTH[month - 1]


def last_day_of_month_leap_year(month: int) -> int:
    return DAYS_OF_MONTH_LEAP_YEAR[month - 1]


def last_day_of_month(year: int, month: int) -> int:
    if month != 2 or not is_leap_year(year):
        return last_day_of_month_common_year(month)
    return 29
