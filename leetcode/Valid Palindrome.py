class Solution:

    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1

        while start < end:

            start_char = s[start].lower()
            end_char = s[end].lower()

            is_acsii_start = start_char.isalpha() or start_char.isalnum()
            is_acsii_end = end_char.isalpha() or end_char.isalnum()

            if not is_acsii_start:
                start += 1

            if not is_acsii_end:
                end -= 1

            if is_acsii_start and is_acsii_end:

                if start_char != end_char:
                    return False
                start += 1
                end -= 1

        return True

print(Solution().isPalindrome('0P'))