def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    start, max_len = 0, 1

    def expand(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        odd_len = expand(i, i)
        even_len = expand(i, i + 1)
        best = max(odd_len, even_len)
        if best > max_len:
            max_len = best
            start = i - (best - 1) // 2

    return s[start : start + max_len]

print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("racecar"))
print(longest_palindromic_substring("abacdfgdcaba"))
print(longest_palindromic_substring("a"))
