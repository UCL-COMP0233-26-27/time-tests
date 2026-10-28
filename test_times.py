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
    # result = compute_overlap_time(large, short) 
    # expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    expected = "dummy info"
    result = "dummy info"
    assert result == expected
    



"""
large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
early = time_range("2000-01-12 10:00:00", "2000-01-12 12:00:00")
late = time_range("2020-01-12 10:00:00", "2020-01-12 12:00:00")
time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

compute_overlap_time(large, short)
compute_overlap_time(early, short)
print(compute_overlap_time(large, short))

expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
expected = "dummy info"
assert compute_overlap_time(large, short) == expected


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    # expected = "dummy info"
    assert result == expected

test_given_input()

if test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))

import os, sys
current_dir
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import game"""