import pytest

from times import compute_overlap_time, time_range


def test_given_input() -> None:
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    # Note that in this particular case, we know that the overlap should be
    # equal to whatever `short` is.
    # So `expected = short` would also work here, but that's generally bad practice,
    # since the point of a test is to test EXPLICITLY (and this behaviour is not)
    # true in the general case.
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]

    assert result == expected


def test_non_overlapping_ranges() -> None:
    first_range = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    second_range = time_range("2010-01-12 12:00:00", "2010-01-12 12:00:00")

    result = compute_overlap_time(first_range, second_range)
    expected = []

    assert result == expected


def test_several_intervals() -> None:
    first_range = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 4)
    second_range = time_range("2010-01-12 10:20:00", "2010-01-12 12:00:00", 3, 300)

    result = compute_overlap_time(first_range, second_range)
    expected = [
        ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
        ("2010-01-12 10:30:00", "2010-01-12 10:45:00"),
        ("2010-01-12 10:45:00", "2010-01-12 10:50:00"),
        ("2010-01-12 10:55:00", "2010-01-12 11:00:00"),
    ]

    assert result == expected


def test_touching_intervals() -> None:
    first_range = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 1)
    second_range = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 1)

    result = compute_overlap_time(first_range, second_range)
    expected = [
        ("2010-01-12 11:00:00", "2010-01-12 11:00:00"),
    ]

    assert result == expected


def test_no_backwards_time_ranges() -> None:
    with pytest.raises(
        ValueError, match="Backwards interval: start time is after end time"
    ):
        time_range("2010-01-12 10:00:00", "2010-01-12 09:00:00")
