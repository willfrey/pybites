from collections import Counter
import os
import re
from typing import List, Tuple
import urllib.request

# prep
tempfile = os.path.join("/tmp", "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read().lower()
del tempfile

# start coding


def get_pybites_top_tags(n: int = 10) -> List[Tuple[str, int]]:
    """Use Counter to get the top 10 PyBites tags from the feed data already
    loaded into the content variable."""
    return Counter(
        match[1] for match in re.finditer(r"<category>(.*?)</category>", content)
    ).most_common(n)
