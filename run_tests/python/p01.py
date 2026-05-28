def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("radar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
print(is_palindrome("Racecar"))
