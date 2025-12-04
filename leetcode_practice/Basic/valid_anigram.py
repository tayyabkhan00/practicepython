def isAnagram(s, t):
    if len(s) != len(t):       # 1
        return False           # 2

    count = {}                 # 3

    for ch in s:               # 4
        count[ch] = count.get(ch, 0) + 1  # 5

    for ch in t:               # 6
        if ch not in count:    # 7
            return False

        count[ch] -= 1         # 8
        
        if count[ch] < 0:      # 9
            return False

    return True                # 10
