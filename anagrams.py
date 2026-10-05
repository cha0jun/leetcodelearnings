'''
Given a list of strings, group the anagrams together. Order within and between groups doesn't matter.
'''

from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    # dict key should be the word following a fix sort
    for word in words:
        sorted_word = "".join(sorted(word))
        groups[sorted_word].append(word)
    
    return list(groups.values())
        



assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"], ["tan","nat"], ["bat"]]
