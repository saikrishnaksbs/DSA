def combinations(s1: str, s2: str):
    if len(s1) == 0:
        print(s2)
        return
    else:
        s2 = s2 + s1[0]
        s1 = s1[1:]
        combinations(s1, s2)
        s2 = s2[:-1]
        combinations(s1, s2)

combinations("abcd", "")