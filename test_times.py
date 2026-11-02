from times import compute_overlap_time, time_range


def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected
def test_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
    assert compute_overlap_time(range1, range2) == []


def test_multiple_intervals_in_both():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2, 60)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:59:30"),
                ("2010-01-12 11:00:30", "2010-01-12 11:30:00")]
    assert compute_overlap_time(range1, range2) == expected


def test_touching_ranges():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    assert compute_overlap_time(range1, range2) == []
