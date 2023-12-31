def get_char_counts(word):
    counts = {}
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def combine(A, B):
    """Combine two count dictionaries into one"""
    a_chars = set(A.keys())
    b_chars = set(B.keys())
    a_and_b = a_chars.intersection(b_chars)
    just_a = a_chars.difference(b_chars)
    just_b = b_chars.difference(a_chars)

    combined = {}
    for a_char in just_a:
        combined[a_char] = A[a_char]

    for b_char in just_b:
        combined[b_char] = B[b_char]

    for both_char in a_and_b:
        combined[both_char] = A[both_char] + B[both_char]

    return combined


def get_character_counts(words):
    character_counts = {}
    for word in words:
        char_counts = get_char_counts(word)
        character_counts = combine(char_counts, character_counts)
    return character_counts


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        character_counts = get_character_counts(words)
        for char, count in character_counts.items():
            if count % n != 0:
                return False
        return True
