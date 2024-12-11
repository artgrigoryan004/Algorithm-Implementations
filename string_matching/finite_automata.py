
def build_dfa(pattern):
    alphabet = set(pattern)
    m = len(pattern)
    dfa = {ch: [0] * m for ch in alphabet}
    dfa[pattern[0]][0] = 1
    x = 0
    for j in range(1, m):
        for ch in alphabet:
            dfa[ch][j] = dfa[ch][x]
        dfa[pattern[j]][j] = j + 1
        x = dfa[pattern[j]][x]
    return dfa

def finite_automata_matching(text, pattern):
    dfa = build_dfa(pattern)
    m, n = len(pattern), len(text)
    state = 0
    for i in range(n):
        if text[i] in dfa:
            state = dfa[text[i]][state]
        if state == m:
            print(f"Pattern found at index {i - m + 1}")

# Example
finite_automata_matching("ababcabcabababd", "ababd")

