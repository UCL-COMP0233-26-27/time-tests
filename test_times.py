import pytest
from times import time_range, compute_overlap_time

@pytest.mark.parametrize(
    "time_range_1, time_range_2, expected",
    [
        # Case 1: Partial overlap
        (
            [("10:00", "12:00")],
            [("11:00", "13:00")],
            [("11:00", "12:00")]
        ),

        # Case 2: No overlap
        (
            [("10:00", "10:30")],
            [("11:00", "11:30")],
            []
        ),

        # Case 3: Multiple overlaps
        (
            [("10:00", "11:00"), ("12:00", "13:00")],
            [("10:30", "11:30"), ("12:30", "13:30")],
            [("10:30", "11:00"), ("12:30", "13:00")]
        ),

        # Case 4: Adjacent intervals
        (
            [("10:00", "11:00")],
            [("11:00", "12:00")],
            []
        )
    ]
)
def test_overlap_cases(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected

# Test 5: Original example
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]

    assert result == expected


# Test 6: Empty input
def test_empty_input():
    range1 = []
    range2 = [("10:00", "11:00")]

    result = compute_overlap_time(range1, range2)

    assert result == []


# Test 7: Backwards time range
def test_backwards_time_range():
    with pytest.raises(ValueError):
        time_range(
            "2010-01-12 12:00:00",
            "2010-01-12 10:00:00"
        )
