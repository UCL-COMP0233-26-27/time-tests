from times import compute_overlap_time, time_range


def test_given_input() -> None:
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    # Note that in this particular case, we know that the overlap should be
    # equal to whatever `short` is.
    # So `expected = short` would also work here, but that's generally bad practice,
    # since the point of a test is to test EXPLICITLY (and this behaviour is not)
    # true in the general case.
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]

    assert result == expected
