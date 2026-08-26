class Solution:
    def isPalindrome(self, s: str) -> bool:
        # log(n/2), Consider Alphanumeric Characters
        s = s.lower().replace(' ', '')
        lengthOfs, i = len(s), 0
        while i < lengthOfs:
            print(i, len(s))
            if not s[i].isalnum():
                s = s.replace(s[i], '', 1)
                lengthOfs -= 1
            i+=1
        print(s)
        l , r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            else: 
                l+=1
                r-=1
        return True