from times import compute_overlap_time, time_range
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)    
    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]
    assert result == expected

def no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)    
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_multiple_intervals():
    range1 = time_range("2010-01-12 10:00:00","2010-01-12 11:00:00",2)
    range2 = time_range("2010-01-12 10:20:00","2010-01-12 11:20:00",2)
    result = compute_overlap_time(range1, range2)

    expected = [
        ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
        ("2010-01-12 10:30:00", "2010-01-12 10:50:00"),
        ("2010-01-12 10:50:00", "2010-01-12 11:00:00")
    ]
    assert result == expected

def start_end_overlap():
    start1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 1)
    start2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 1)
    result = compute_overlap_time(start1, start2)
    expected = [("2010-01-12 11:00:00", "2010-01-12 11:00:00")]
    assert result == expected