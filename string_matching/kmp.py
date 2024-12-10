
def kmp_search(text, pattern):
    def kmp_preprocess(pattern):
        m = len(pattern)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    lps = kmp_preprocess(pattern)
    n, m = len(text), len(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i - m + 1}")
            j = lps[j - 1]

# Example
kmp_search("ababcabcabababd", "ababd")

