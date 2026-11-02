from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 12:00:00"
    )
    short = time_range(
        "2010-01-12 10:30:00",
        "2010-01-12 10:45:00",
        2,
        60
    )

    result = compute_overlap_time(large, short)

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]

    assert result == expected


# Test 1: Two time ranges do not overlap
def test_no_overlap():
    range1 = [
        ("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    ]

    range2 = [
        ("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    ]

    result = compute_overlap_time(range1, range2)

    expected = []

    assert result == expected


# Test 2: Both time ranges contain several intervals
def test_multiple_intervals():
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


# Test 3: One range ends exactly when the other starts
def test_touching_ranges():
    range1 = [
        ("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    ]

    range2 = [
        ("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    ]

    result = compute_overlap_time(range1, range2)

    expected = []

    assert result == expected