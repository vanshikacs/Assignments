def group_anagrams(strs):
    
    anagrams = {}
    
    for s in strs:
    
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    
    return list(anagrams.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat", "tab", "cat"]))