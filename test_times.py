import pytest
from times import time_range, compute_overlap_time

@pytest.mark.parametrize(
    "range1, range2, expected",
    [
        # Test 1: Original example
        pytest.param(
            time_range(
                "2010-01-12 10:00:00",
                "2010-01-12 12:00:00"
            ),
            time_range(
                "2010-01-12 10:30:00",
                "2010-01-12 10:45:00",
                2,
                60
            ),
            [
                ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
            ],
            id="Original example",
        ),

        # Test 2: Empty input
        pytest.param(
            [],
            [("2010-01-12 10:00:00", "2010-01-12 11:00:00")],
            [],
            id="Empty input",
        ),

        # Test 3: Partial overlap
        pytest.param(
            [("2010-01-12 10:00:00", "2010-01-12 12:00:00")],
            [("2010-01-12 11:00:00", "2010-01-12 13:00:00")],
            [("2010-01-12 11:00:00", "2010-01-12 12:00:00")],
            id="Partial overlap",
        ),

        # Test 4: No overlap
        pytest.param(
            [("2010-01-12 10:00:00", "2010-01-12 10:30:00")],
            [("2010-01-12 11:00:00", "2010-01-12 11:30:00")],
            [],
            id="No overlap",
        ),

        # Test 5: Multiple overlaps
        pytest.param(
            [
                ("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
                ("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
            ],
            [
                ("2010-01-12 10:30:00", "2010-01-12 11:30:00"),
                ("2010-01-12 12:30:00", "2010-01-12 13:30:00"),
            ],
            [
                ("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
                ("2010-01-12 12:30:00", "2010-01-12 13:00:00"),
            ],
            id="Multiple overlaps",
        ),

        # Test 6: Adjacent intervals
        pytest.param(
            [("2010-01-12 10:00:00", "2010-01-12 11:00:00")],
            [("2010-01-12 11:00:00", "2010-01-12 12:00:00")],
            [
                ("2010-01-12 11:00:00", "2010-01-12 11:00:00")
            ],
            id="Adjacent intervals",
        ),
    ],
)

def test_compute_overlap_time(range1, range2, expected):
    result = compute_overlap_time(range1, range2)
    assert result == expected

def test_time_range_backwords():
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")