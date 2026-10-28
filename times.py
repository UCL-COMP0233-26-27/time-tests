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

# exploration
# running the functions
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

print(test_given_input())