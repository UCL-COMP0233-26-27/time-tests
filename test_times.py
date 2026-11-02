import times

def test_given_input():
    # Call the function from times.py
    result = times.overlap_time(...) 
    # Set your expected output (initially based on the program's output)
    expected = ... 
    assert result == expected

from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected


    #cd timetest/time-tests
    #pip install pytest
    #python -m pytest