from times import compute_overlap_time, time_range

from pytest import raises

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    # short returns 2 tuples 10:30 to 10:37 and 10:38 to 10:45
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60) # 15 min time interval split into 2 with 60 sec interval
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")] # list of 2 tuples
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2010-01-12 13:00:00", "2010-01-12 15:00:00")
    expected = []
    assert compute_overlap_time(first, second) == expected

def test_touch_intervals ():
    # choose specific values to check function
    first_range = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second_range = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    expected = time_range("2010-01-12 12:00:00", "2010-01-12 12:00:00") # overlap is exaclty when first one ends and second one starts
    assert compute_overlap_time(first_range, second_range) == expected

def test_start_not_before_end ():
    start_time = "2010-01-12 12:00:00" # need correct format, this one is a range
    end_time = "2010-01-12 10:00:00"

    # with blocks are a catching technique basically
    with raises (ValueError, match = "Start time must be before end time"): # give error type, and match is the message
        # have only 1 function call in raise block
        time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0)
