from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

# create a test each in test_times.py for:
    # two time ranges that do not overlap
    # two time ranges that both contain several intervals each
    # two time ranges that end exactly at the same time when the other starts

def no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60) # list containing two tuples - first is 10:30 - 10:37, second is 10:38 - 10:45
    result = compute_overlap_time(large, short) 
    assert result[0][1] < result[1][0]

def correct_intervals():
    large = [("2010-01-12 10:00:00", "2010-01-12 10:10:00"), ("2010-01-12 10:15:00", "2010-01-12 10:25:00"), ("2010-01-12 10:40:00", "2010-01-12 10:50:00")]
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    # [ (10:30, 10:37), (10:38, 10:45)], [(10:00, 10:10), (10:15, 10:25), (10:40, 10:50)]
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:40:00', '2010-01-12 10:45:00')]
    assert result == expected

def no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2) 
    result = compute_overlap_time(large, short) 
    assert result[0][1] == result[1][0]
    