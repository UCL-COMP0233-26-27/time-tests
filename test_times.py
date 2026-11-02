from times import time_range, compute_overlap_time
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00",
                       "2010-01-12 12:00:00")

    short = time_range("2010-01-12 10:30:00",
                       "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)

    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]

    assert result == expected


def test_no_overlap():
    large1 = time_range("2010-01-12 10:00:00",
                        "2010-01-12 12:00:00")

    short1 = time_range("2010-01-12 12:30:00",
                        "2010-01-12 12:45:00", 2, 60)

    result1 = compute_overlap_time(large1, short1)

    expected1 = []

    assert result1 == expected1



def test_multiple_intervals():
    range1 = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 13:00:00",
        2,
        3600
    )

    range2 = time_range(
        "2010-01-12 10:30:00",
        "2010-01-12 13:30:00",
        2,
        3600
    )

    result = compute_overlap_time(range1, range2)

    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 11:00:00'),
        ('2010-01-12 12:30:00', '2010-01-12 13:00:00')
    ]

    assert result == expected




def test_touching_ranges():
    range1 = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 11:00:00"
    )

    range2 = time_range(
        "2010-01-12 11:00:00",
        "2010-01-12 12:00:00"
    )

    result = compute_overlap_time(range1, range2)
    expected = []

    assert result == expected

#2026 11.2


def test_backwards_time_range():
    with pytest.raises(ValueError):
        time_range(
            "2010-01-12 12:00:00",
            "2010-01-12 10:00:00"
        )