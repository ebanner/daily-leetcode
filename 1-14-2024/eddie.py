def get_counts(word):
    counts = {}
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counts1 = get_counts(word1)
        counts2 = get_counts(word2)
        
        return (counts1.keys() == counts2.keys()) and \
            (sorted(counts1.values()) == sorted(counts2.values()))
