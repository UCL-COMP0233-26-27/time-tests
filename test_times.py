import pytest
from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    # calculate the overlapping time intervals
    result = compute_overlap_time(large, short)

    # expected result
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]

    # check whether the actual result matches the expected result
    assert result == expected

def test_empty_input():
    range1 = []
    range2 = [("10:00", "11:00")]

    result = compute_overlap_time(range1, range2)
    assert result == []

def test_partial_overlap():
    range1 = [("10:00", "12:00")]
    range2 = [("11:00", "13:00")]

    result = compute_overlap_time(range1, range2)
    expected = [("11:00", "12:00")]

    assert result == expected

# test case for no overlap
def test_no_overlap():
    range1 = [("10:00", "10:30")]
    range2 = [("11:00", "11:30")]

    assert compute_overlap_time(range1, range2) == []

# test case for both several overlapping intervals
def test_multiple_overlaps():
    range1 = [("10:00", "11:00"), ("12:00", "13:00")]
    range2 = [("10:30", "11:30"), ("12:30", "13:30")]

    result = compute_overlap_time(range1, range2)
    expected = [("10:30", "11:00"), ("12:30", "13:00")]

    assert result == expected

# test case for adjacent intervals
def test_adjacent_intervals():
    range1 = [("10:00", "11:00")]
    range2 = [("11:00", "12:00")]

    result = compute_overlap_time(range1, range2)
    assert result == []

def test_time_range_backwords():
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")