import os
from pathlib import Path
import re
from typing import Counter
import urllib.request

# data provided
STOP_WORDS_FILE_PATH = Path("/tmp", "stopwords")
urllib.request.urlretrieve("http://bit.ly/2EuvyHB", STOP_WORDS_FILE_PATH)

HARRY_TEXT_FILE_PATH = Path("/tmp", "harry")
urllib.request.urlretrieve("http://bit.ly/2C6RzuR", HARRY_TEXT_FILE_PATH)


def get_harry_most_common_word() -> str:
    stop_words = STOP_WORDS_FILE_PATH.read_text().splitlines()
    text = HARRY_TEXT_FILE_PATH.read_text()
    text = re.sub(r"[^A-Z0-9\s]", "", text, flags=re.IGNORECASE)
    words = text.split()
    word_counts = Counter(w for w in words if w not in stop_words)
    return word_counts.most_common(1)[0]
