import re
from collections import Counter

def word_frequency(text: str) -> dict:
    words = re.findall(r'\b[a-z]+\b', text.lower())
    freq = Counter(words)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

paragraph = "The quick brown fox jumps over the lazy dog. The dog barked at the fox."
result = word_frequency(paragraph)
print(result)
