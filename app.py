def is_palindrome(text):
    processed = "".join(c.lower() for c in text if c.isalnum())
    return processed == processed[::-1]

# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True