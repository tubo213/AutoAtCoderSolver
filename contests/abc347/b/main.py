def count_distinct_substrings(S):
    n = len(S)

    # Build suffixes and suffix array
    suffixes = sorted([(S[i:], i) for i in range(n)])
    sa = [suffix[1] for suffix in suffixes]

    # Build LCP array
    rank = [0] * n
    for i, suff in enumerate(sa):
        rank[suff] = i

    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and S[i + h] == S[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1

    # Calculate number of distinct non-empty substrings
    num_distinct_substrings = 0
    for i in range(n):
        num_distinct_substrings += (n - sa[i]) - lcp[i]

    return num_distinct_substrings


if __name__ == "__main__":
    import sys

    input = sys.stdin.read().strip()
    print(count_distinct_substrings(input))
