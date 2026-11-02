import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time



from times import TimeRange  # or your respective time range functions/classes


def test_time_ranges_no_overlap():
    """Test two time ranges that do not overlap at all."""
    range1 = TimeRange("09:00", "10:00")
    range2 = TimeRange("11:00", "12:00")
    assert not range1.overlaps(range2)  # or your overlap checking function


def test_time_ranges_multiple_intervals():
    """Test two time ranges that both contain several intervals/sub-ranges."""
    # asuming your implementation handles composite ranges or multiple intervals
    range1 = TimeRange([("09:00", "10:00"), ("11:00", "12:00")])
    range2 = TimeRange([("09:30", "10:30"), ("11:30", "12:30")])
    
    intersect = range1.intersection(range2)
    assert len(intersect.intervals) == 2


def test_time_ranges_touching_endpoints():
    """Test two time ranges where one ends exactly at the time the other starts."""
    range1 = TimeRange("09:00", "10:00")
    range2 = TimeRange("10:00", "11:00")
    
    # Depending on your specification, touching at a boundary might be 
    # considered overlapping or strictly non-overlapping. Adjust as needed:
    assert not range1.overlaps(range2)

    def test_touching_intervals_2(): # design tests to assess computing overlap time
        first_range = [("2010-01-12 00:00:00", "2010-01-13 12:00:00")]
        second_Range = [("2010-01-12 12:00:00", "2010-01-12 12:00:00" )]

        expected+[("2010-01-12 00:00:00", "2010-01-12 12:00:00" )]
        result = compute_overlap_time(first_range, second_Range)

        assert expected == result

# pytest will assess all functions


import pytest

def time_range(start_time, end_time):
    if end_time < start_time:
        raise ValueError("end_time cannot be earlier than start_time")
    # ... rest of your code ...

def test_time_range_backwards():
    with pytest.raises(ValueError, match="end_time cannot be earlier than start_time"):
        time_range(start_time ="2026-03-05 12:00", end_time ="2026-03-01 12:00")


import pytest

def test_start_notbefore_end()
    start_time = "2010-01-02 00:00:00"
    end_time = "2010-01-01 00:00:00"

    with pytest.raises(ValueError, match = "Start time must come after end time"):
        ##only one command error should be raised in python raises, 
        # also why you specify the type of error
        time_range(start_time, end_time)


