import re

def find_word(text, word):
    matches = re.findall(word, text)
    return len(matches)
