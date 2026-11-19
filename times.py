import datetime
import os
import requests


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    if start_time_s >= end_time_s:
        raise ValueError("Backwards interval: start time is after end time.")
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
            if low <= high:
                overlap_time.append((low, high))
    return overlap_time



def iss_passes(
    latitude=56,
    longitude=0,
    altitude=0,
    days=5,
    min_visibility=50,
):
    """Get visible ISS passes as pairs of UTC time strings."""

    api_key = os.environ["N2YO_API_KEY"]

    base_url = "https://api.n2yo.com/rest/v1/satellite/visualpasses"

    url = (
        f"{base_url}/25544/{latitude}/{longitude}/"
        f"{altitude}/{days}/{min_visibility}/&apiKey={api_key}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    pass_data = response.json()["passes"]

    intervals = []
    time_format = "%Y-%m-%d %H:%M:%S"

    for passage in pass_data:
        start_time = datetime.datetime.fromtimestamp(
            passage["startUTC"],
            tz=datetime.timezone.utc,
        )

        end_time = datetime.datetime.fromtimestamp(
            passage["endUTC"],
            tz=datetime.timezone.utc,
        )

        start_string = start_time.strftime(time_format)
        end_string = end_time.strftime(time_format)

        intervals.append((start_string, end_string))

    return intervals
