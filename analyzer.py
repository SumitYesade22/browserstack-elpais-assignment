import re
from collections import Counter


def find_repeated_words(titles, min_occurrences=3):
    """
    titles: list of translated title strings
    min_occurrences: threshold (default = 3 because >2)
    """

    all_words = []

    for title in titles:
       
        title = title.lower()

       
        title = re.sub(r"[^a-z\s]", "", title)

       
        words = title.split()

        all_words.extend(words)

 
    word_counts = Counter(all_words)

    
    repeated = {
        word: count
        for word, count in word_counts.items()
        if count >= min_occurrences
    }

    return repeated
