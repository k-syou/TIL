def broute_force(text, pattern):
    i = j = 0
    while i < len(text) and j < len(pattern):
        if text[j + i] == pattern[j]:
            j += 1
        else:
            i += 1
            j = 0
        # if text[i] == pattern[j]:
        #     i += 1
        #     j += 1
        # else:
        #     i = i - j + 1
        #     j = 0

    if j >= len(pattern):
        return i
    return -1


text = "SFGHAHTRSTYDVHBBVN"
pattern = "APPLE"
print(broute_force(text, pattern))
