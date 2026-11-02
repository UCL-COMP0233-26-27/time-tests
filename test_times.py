import pytest
from times import time_range, compute_overlap_time

import yaml
from pathlib import Path


# Read test data from YAML
fixture_path = Path(__file__).with_name("fixture.yaml")

with fixture_path.open("r", encoding="utf-8") as file:
    fixture_data = yaml.safe_load(file)

test_cases = []

for case in fixture_data:
    for name, data in case.items():
        range1 = [tuple(item) for item in data["time_range_1"]]
        range2 = [tuple(item) for item in data["time_range_2"]]
        expected = [tuple(item) for item in data["expected"]]

        test_cases.append(
            pytest.param(range1, range2, expected, id=name)
        )


@pytest.mark.parametrize(
    "time_range_1, time_range_2, expected",
    test_cases
)
def test_overlap_cases(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected

# Test 5: Original example
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]

    assert result == expected


# Test 6: Empty input
def test_empty_input():
    range1 = []
    range2 = [("10:00", "11:00")]

    result = compute_overlap_time(range1, range2)

    assert result == []


# Test 7: Backwards time range
def test_backwards_time_range():
    with pytest.raises(ValueError):
        time_range(
            "2010-01-12 12:00:00",
            "2010-01-12 10:00:00"
        )
