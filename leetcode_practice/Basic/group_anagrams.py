def groupAnagrams(strs):
    groups = {}                      # 1

    for word in strs:                # 2
        count = [0] * 26             # 3
        
        for ch in word:              # 4
            count[ord(ch) - ord('a')] += 1  # 5
        
        key = tuple(count)           # 6

        if key not in groups:        # 7
            groups[key] = []         # 8
        
        groups[key].append(word)     # 9

    return list(groups.values())     # 10
