
def naive_string_matching(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print(f"Pattern found at index {i}")

# Example
naive_string_matching("ababcabcabababd", "ababd")

