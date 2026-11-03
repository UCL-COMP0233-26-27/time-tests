
import datetime
from unittest.mock import patch

import pytest

from times import time_range, compute_overlap_time, iss_passes


# Test 1: Basic time range
def test_time_range():
    result = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 12:00:00"
    )

    assert result == [
        ("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    ]


# Test 2: Invalid time range
def test_backwards():
    with pytest.raises(ValueError):
        time_range(
            "2010-01-12 12:00:00",
            "2010-01-12 10:00:00"
        )


# Test 3: Overlapping intervals
def test_overlap():
    large = time_range(
        "2010-01-12 10:00:00",
        "2010-01-12 12:00:00"
    )

    short = time_range(
        "2010-01-12 10:30:00",
        "2010-01-12 10:45:00"
    )

    result = compute_overlap_time(large, short)

    assert result == [
        ("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    ]


# Test 4: Mock ISS API request
def test_iss_passes():
    fake_data = {
        "passes": [
            {
                "startUTC": 1700000000,
                "endUTC": 1700000300
            }
        ]
    }

    with patch("times.requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_data

        result = iss_passes("fake-api-key")

        expected_start = datetime.datetime.fromtimestamp(
            1700000000
        ).strftime("%Y-%m-%d %H:%M:%S")

        expected_end = datetime.datetime.fromtimestamp(
            1700000300
        ).strftime("%Y-%m-%d %H:%M:%S")

        assert result == [(expected_start, expected_end)]

        mock_get.assert_called_once()
        mock_get.return_value.raise_for_status.assert_called_once()


# Test 5: ISS API returns no passes
def test_iss_passes_empty():
    fake_data = {
        "passes": []
    }

    with patch("times.requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_data

        result = iss_passes("fake-api-key")

        assert result == []
        mock_get.assert_called_once()
