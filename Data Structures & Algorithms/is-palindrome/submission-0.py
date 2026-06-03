class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(char for char in s.lower() if char.isalnum())

        if s == s[::-1]:
            return True
        return False
        