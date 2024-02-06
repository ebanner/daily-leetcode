def insert(str, anagram_dict):
    sorted_str = ''.join(sorted(str))
    if sorted_str in anagram_dict:
        anagram_dict[sorted_str].append(str)
    else:
        anagram_dict[sorted_str] = [str]
    return anagram_dict


def convert(anagram_dict):
    anagram_groups = []
    for anagram_group in anagram_dict.values():
        anagram_groups.append(anagram_group)
    return anagram_groups


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for str in strs:
            anagram_dict = insert(str, anagram_dict)
        anagram_groups = convert(anagram_dict)
        return anagram_groups

