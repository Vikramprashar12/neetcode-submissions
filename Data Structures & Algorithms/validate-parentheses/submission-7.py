class Solution:
    def isValid(self, s: str) -> bool:
        
        helper = []
        for c in s:
            print(c)
            if c == "{" or c == "(" or c == "[":
                helper.append(c)
            elif not helper:
                return False
            elif (c == "}" and helper[-1] != "{") or (c == ")" and helper[-1] != "(") or (c == "]" and helper[-1] != "["):
                return False
            else:
                helper.pop()
                
        return True if not helper else False

