import pytest

from deltat_t.deltadate import Time


@pytest.mark.parametrize(
    "h1,m1,s1,h2,m2,s2",
    [
        (
            0,
            0,
            0,
            0,
            0,
            0,
        ),
    ],
)
def test_time_equals(
    h1,
    m1,
    s1,
    h2,
    m2,
    s2,
):
    t1 = Time(h1, m1, s1)
    t2 = Time(h2, m2, s2)

    assert t1 == t2


@pytest.mark.parametrize(
    "h1,m1,s1,h2,m2,s2",
    [
        (
            0,
            0,
            0,
            0,
            0,
            1,
        ),
    ],
)
def test_time_not_equals(
    h1,
    m1,
    s1,
    h2,
    m2,
    s2,
):
    t1 = Time(h1, m1, s1)
    t2 = Time(h2, m2, s2)

    assert t1 != t2


@pytest.mark.parametrize(
    "h1,m1,s1,h2,m2,s2",
    [
        (
            0,
            0,
            0,
            0,
            0,
            1,
        ),
        (0, 1, 10, 0, 2, 9),
    ],
)
def test_time_lt(h1, m1, s1, h2, m2, s2):
    t1 = Time(h1, m1, s1)
    t2 = Time(h2, m2, s2)

    assert t1 < t2
