from times import time_range, compute_overlap_time
import pytest


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    no_overlap1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    no_overlap2 = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)

    result1 = compute_overlap_time(no_overlap1, no_overlap2)
    result2 = compute_overlap_time(no_overlap2, no_overlap1)
    expected = []
    assert result1 == expected and result2 == expected

def test_multiple_overlap():
    three_intervals = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 120)
    two_intervals = time_range("2010-01-12 10:10:00", "2010-01-12 12:45:00", 2, 60)

    result = compute_overlap_time(three_intervals, two_intervals)
    expected = [('2010-01-12 10:10:00', '2010-01-12 10:58:40'), ('2010-01-12 11:00:40', '2010-01-12 11:27:00'), ('2010-01-12 11:28:00', '2010-01-12 11:59:20'), ('2010-01-12 12:01:20', '2010-01-12 12:45:00')]
    assert result == expected

def test_time_normal():
    with pytest.raises(ValueError) as excinfo:
        backwards_time = time_range("2010-01-11 10:00:00", "2010-01-10 13:00:00")
        normal_time = time_range("2010-01-12 10:10:00", "2010-01-12 12:45:00", 2, 60)
        
        compute_overlap_time(backwards_time, normal_time)

        assert excinfo is ValueError