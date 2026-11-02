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

# test no overlap
def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    early = time_range("2000-01-12 10:00:00", "2000-01-12 12:00:00")
    # short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, early) 
    # expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    expected = []
    # result = "dummy info"
    assert result == expected

# test several intervals each
def test_several_intervals():
    four_times = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 4, 30)   
    three_times = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 3, 60)
    expected = [('2010-01-12 10:30:15', '2010-01-12 10:44:52'), ('2010-01-12 10:45:22', '2010-01-12 10:49:20'), ('2010-01-12 10:50:20', '2010-01-12 11:00:00')]
    # [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    result = compute_overlap_time(four_times, three_times) 
    # result = "dummy info"
    assert result == expected


##  two time ranges that end exactly at the same time when the other starts
def test_same_start_endtime(): 
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    next = time_range("2010-01-12 12:00:00", "2010-01-12 12:30:00")
    expected = []
    actual = compute_overlap_time(large, next)
    assert actual == expected 


"""
create a test each in test_times.py for:

    two time ranges that do not overlap

    two time ranges that both contain several intervals each

    two time ranges that end exactly at the same time when the other starts

"""



