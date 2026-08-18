def longest_common_prefix(strs):
    if not strs:
        return ""

    first = strs[0]

    for i in range(len(first)):
        char = first[i]

        for other in strs[1:]:
            if not (i < len(other) and other[i] == char):
                return first[:i]

    return first