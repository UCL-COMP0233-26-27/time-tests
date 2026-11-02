# import the overlap_time functions
from times import time_range, compute_overlap_time 
import pytest

def test_given_input ():

    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    

    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]
    assert result == expected 

def test_no_overlap ():
    
    # make sure the time ranges do not overlap
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 12:30:00", "2010-01-12 13:45:00")
    

    result = compute_overlap_time(range1, range2)

    expected = []

    assert result == expected


def test_multiple_intervals():

    # make sure there is an overlap of time intervals 
    # 10:00 - 10:30, 11:00 - 11:30
    # 10:15 - 10:45, 11:15 - 11:45
    range1 = [
        ("2010-01-12 10:00:00", "2010-01-12 10:30:00"),
        ("2010-01-12 11:00:00", "2010-01-12 11:30:00")
    ]

    range2 = [
        ("2010-01-12 10:15:00", "2010-01-12 10:45:00"),
        ("2010-01-12 11:15:00", "2010-01-12 11:45:00")
    ]

    result = compute_overlap_time(range1, range2)

    expected = [
        ("2010-01-12 10:15:00", "2010-01-12 10:30:00"),
        ("2010-01-12 11:15:00", "2010-01-12 11:30:00")
    ]

    assert result == expected

def test_backwards_time_range():
    with pytest.raises(ValueError, match="End time cannot be before start time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

