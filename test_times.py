import pytest
from times import compute_overlap_time, time_range
# def test_given_input():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)    
#     result = compute_overlap_time(large, short)
#     expected = [
#         ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
#         ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
#     ]
#     assert result == expected

# def no_overlap():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)    
#     result = compute_overlap_time(large, short)
#     expected = []
#     assert result == expected

# def test_multiple_intervals():
#     range1 = time_range("2010-01-12 10:00:00","2010-01-12 11:00:00",2)
#     range2 = time_range("2010-01-12 10:20:00","2010-01-12 11:20:00",2)
#     result = compute_overlap_time(range1, range2)

#     expected = [
#         ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
#         ("2010-01-12 10:30:00", "2010-01-12 10:50:00"),
#         ("2010-01-12 10:50:00", "2010-01-12 11:00:00")
#     ]
#     assert result == expected

# def start_end_overlap():
#     start1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 1)
#     start2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 1)
#     result = compute_overlap_time(start1, start2)
#     expected = [("2010-01-12 11:00:00", "2010-01-12 11:00:00")]
#     assert result == expected

# import pytest
# def test_no_backwards_time_ranges():
#     with pytest.raises(ValueError, match="Backwards interval: start time is after end time"):
#         time_range("2010-01-12 10:00:00","2010-01-12 09:00:00")
import pytest
@pytest.mark.parametrize("time_range_1, time_range_2, expected",
                         [
        # Test 1: Original example
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [
                ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
            ],
        ),

        # Test 2: No overlap
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
            [],
        ),

        # Test 3: Multiple intervals
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2),
            time_range("2010-01-12 10:20:00", "2010-01-12 11:20:00", 2),
            [
                ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
                ("2010-01-12 10:30:00", "2010-01-12 10:50:00"),
                ("2010-01-12 10:50:00", "2010-01-12 11:00:00"),
            ],
        ),

        # Test 4: Touching intervals
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"),
            [
                ("2010-01-12 11:00:00", "2010-01-12 11:00:00"),
            ],
        ),
    ],
)
def test_compute_overlap_time(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected


def test_no_backwards_time_ranges():
    with pytest.raises(ValueError, match="Backwards interval: start time is after end time"):
        time_range("2010-01-12 10:00:00", "2010-01-12 09:00:00")
