import pytest
import yaml
from times import time_range, compute_overlap_time

with open("fixture.yaml", "r") as file:
    test_data = yaml.safe_load(file)

@pytest.mark.parametrize(
    "range1, range2, expected",
    [
        pytest.param(
            case["time_range_1"],
            case["time_range_2"],
            [tuple(interval) for interval in case["expected"]],
            id=name,
        )
        for name, case in test_data.items()
    ],
)

def test_compute_overlap_time(range1, range2, expected):
    result = compute_overlap_time(range1, range2)
    assert result == expected

def test_time_range_backwords():
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

def test_time_range():
    result = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    expected = [("2010-01-12 10:00:00", "2010-01-12 12:00:00")]

    assert result == expected