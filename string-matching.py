def naive(string, pattern):
    n = len(string)
    m = len(pattern)

    matches = []

    for s in range(n-m):
        if string[s:s+m] == pattern:
            matches.append((s, s+m))

    return matches


def rabin_karp(string, pattern):
    d = 256
    q = 101

    n = len(string)
    m = len(pattern)

    h = pow(d, m-1, q)
    p = 0
    t = 0

    matches = []

    for s in range(m):
        p = (d*p + ord(pattern[s])) % q
        t = (d*t + ord(string[s])) % q

    for s in range(n-m):
        if p == t:
            if string[s:s+m] == pattern:
                matches.append((s, s+m))
        if s < n-m:
            t = (d * (t - ord(string[s]) * h) + ord(string[s+m])) % q

    return matches


def transition_function(pattern):
    d = 256
    m = len(pattern)
    table = {}

    for q in range(m):
        for a in range(d):
            k = min(m, q+1)
            while not (pattern[:q]+chr(a))[-k:] == pattern[:k]:
                k -= 1
            table[q, a] = k

    return table


def finite_automota(string, pattern):
    n = len(string)
    m = len(pattern)

    table = transition_function(pattern)

    matches = []

    q = 0
    for s in range(n):
        q = max(0, table[q, ord(string[s])])
        if q == m:
            q = 0
            matches.append((s-m+1, s+1))

    return matches
