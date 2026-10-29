import pytest

from times import TimeIntervals, compute_overlap_time, time_range


@pytest.mark.parametrize(
    ("range1", "range2", "expected"),
    [
        pytest.param(
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [
                ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
            ],
            id="Given values (from original code)",
        ),
        pytest.param(
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            time_range("2010-01-12 12:00:00", "2010-01-12 12:00:00"),
            [],
            id="No overlap",
        ),
        pytest.param(
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 4),
            time_range("2010-01-12 10:20:00", "2010-01-12 12:00:00", 3, 300),
            [
                ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
                ("2010-01-12 10:30:00", "2010-01-12 10:45:00"),
                ("2010-01-12 10:45:00", "2010-01-12 10:50:00"),
                ("2010-01-12 10:55:00", "2010-01-12 11:00:00"),
            ],
            id="Several intervals in each time range",
        ),
        pytest.param(
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 1),
            time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 1),
            [
                ("2010-01-12 11:00:00", "2010-01-12 11:00:00"),
            ],
            id="Touching intervals",
        ),
    ],
)
def test_compute_overlap_time(
    range1: TimeIntervals,
    range2: TimeIntervals,
    expected: TimeIntervals,
) -> None:
    """Test `compute_overlap_time` under various circumstances."""
    result = compute_overlap_time(range1, range2)

    assert result == expected


def test_no_backwards_time_ranges() -> None:
    with pytest.raises(
        ValueError, match="Backwards interval: start time is after end time"
    ):
        time_range("2010-01-12 10:00:00", "2010-01-12 09:00:00")
