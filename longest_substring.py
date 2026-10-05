'''
Return the length of the longest substring with no repeated characters.
'''

def length_of_longest(s:str) -> int:
    seen = set()
    left = 0
    highest = 0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        highest = max(highest, right - left + 1)
    
    return highest
    

assert length_of_longest("abcabcbb") == 3   # "abc"
assert length_of_longest("bbbbb") == 1
assert length_of_longest("pwwkew") == 3      # "wke"