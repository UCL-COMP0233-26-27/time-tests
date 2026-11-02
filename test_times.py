from times import time_range, compute_overlap_time
from pytest import raises
import pytest
from pathlib import Path
import yaml
'''
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

def test_no_overlap():
    range1 = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 10:30:00"
    )
    range2 = time_range(
        "2010-01-12 11:00:00",
        "2010-01-12 11:30:00"
    )

    result = compute_overlap_time(range1, range2)

    expected = []
    assert result == expected
    
def test_intervals():
    range1 = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 12:00:00",
        2
    )

    range2 = time_range(
        "2010-01-12 10:30:00",
        "2010-01-12 11:30:00",
        2
    )

    result = compute_overlap_time(range1, range2)

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
        ("2010-01-12 11:00:00", "2010-01-12 11:30:00")
    ]
    assert result == expected

def test_same_times():
    range1 = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 11:00:00"
    )

    range2 = time_range(
        "2010-01-12 11:00:00",
        "2010-01-12 12:00:00"
    )

    result = compute_overlap_time(range1, range2)

    expected = []
    assert result == expected
'''

'''
@pytest.mark.parametrize(
    "time_range1, time_range2, expected",
    [
        (
            time_range(
                "2010-01-12 10:00:00",
                "2010-01-12 12:00:00"
            ),
            time_range(
                "2010-01-12 10:30:00",
                "2010-01-12 10:45:00",
                2,
                60
            ),
            [
                ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
            ]
        ),
        (
            time_range(
                "2010-01-12 10:00:00",
                "2010-01-12 10:30:00"
            ),
            time_range(
                "2010-01-12 11:00:00",
                "2010-01-12 11:30:00"
            ),
            []
        ),
        (
            time_range(
                "2010-01-12 10:00:00",
                "2010-01-12 12:00:00",
                2
            ),
            time_range(
                "2010-01-12 10:30:00",
                "2010-01-12 11:30:00",
                2
            ),
            [
                ("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
                ("2010-01-12 11:00:00", "2010-01-12 11:30:00")
            ]
        ),
        (
            time_range(
                "2010-01-12 10:00:00",
                "2010-01-12 11:00:00"
            ),
            time_range(
                "2010-01-12 11:00:00",
                "2010-01-12 12:00:00"
            ),
            []
        )
    ]
)
def test_compute_overlap_time(time_range1, time_range2, expected):
    result = compute_overlap_time(time_range1, time_range2)
    assert result == expected
'''



fixture_path = Path(__file__).with_name("fixture.yaml")

with fixture_path.open("r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

test_cases = []

for item in data:
    for name, case in item.items():
        range1 = time_range(*case["time_range_1"])
        range2 = time_range(*case["time_range_2"])
        expected = [tuple(pair) for pair in case["expected"]]

        test_cases.append(
            pytest.param(range1, range2, expected, id=name)
        )


@pytest.mark.parametrize(
    "time_range1, time_range2, expected",
    test_cases
)
def test_compute_overlap_time(time_range1, time_range2, expected):
    result = compute_overlap_time(time_range1, time_range2)
    assert result == expected


def test_invalid_time_range():
    with raises(ValueError):
        time_range(
            "2010-01-12 12:00:00",
            "2010-01-12 10:00:00"
        )