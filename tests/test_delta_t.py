import pytest

from deltat_t.deltadate import Date, DDate


@pytest.mark.parametrize(
    "y1,m1,d1,y2,m2,d2,y,m,d",
    [
        (2019, 1, 1, 2019, 1, 1, 0, 0, 0),
        (2019, 1, 1, 2019, 1, 2, 0, 0, 1),
        (2019, 1, 1, 2020, 1, 1, 1, 0, 0),
        (2019, 1, 1, 2020, 2, 1, 1, 1, 0),
        (2019, 1, 1, 2020, 2, 2, 1, 1, 1),
        (2019, 1, 1, 2020, 2, 3, 1, 1, 2),
        (2019, 2, 10, 2019, 1, 20, 0, 0, 21),
        (2020, 3, 1, 2020, 2, 1, 0, 1, 0),
        (2020, 3, 1, 2020, 2, 20, 0, 0, 10),
    ],
)
def test_date(y1, m1, d1, y2, m2, d2, y, m, d):
    d1 = Date(y1, m1, d1)
    d2 = Date(y2, m2, d2)
    dd = DDate(d1, d2)
    ry, rm, rd = dd.diff()

    assert ry == y
    assert rm == m
    assert rd == d
