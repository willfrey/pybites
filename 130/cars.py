from collections import Counter

import requests

DATA_URL = "https://bit.ly/2Ov65SJ"

# pre-work: load JSON data into program

with requests.Session() as s:
    DATA = s.get(DATA_URL).json()


# your turn:
def most_prolific_automaker(year: str) -> str:
    """Given year 'year' return the automaker that released the highest number
    of new car models."""
    automakers_by_year = [
        item.get("automaker") for item in DATA if item.get("year") == year
    ]
    automaker_count = Counter(automakers_by_year)
    (automaker, _), *_ = automaker_count.most_common()
    return automaker


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year', return a set of models (a
    'set' to avoid duplicate models)"""
    pass
