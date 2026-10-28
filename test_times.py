# set up
# import datetime
# import functions to test
# from .times.py import time_range
from times import time_range
from times import compute_overlap_time

# testing the info
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    #expected = "dummy info"
    #result = "dummy info"
    assert result == expected
    
def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    early = time_range("2000-01-12 10:00:00", "2000-01-12 12:00:00")
    # short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, early) 
    # expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    expected = 'No overlap'
    # result = "dummy info"
    assert result == expected
