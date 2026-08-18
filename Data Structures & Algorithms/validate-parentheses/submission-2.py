class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        accepted = ["[]","{}","()"]

        for c in s:
            if (c == "[" or c  == "(" or c == "{"):
                stack.append(c)
                continue
            if (c == "]" and stack):
                popped = stack.pop()
                if popped != "[":
                    return False
            elif(c == "}" and stack):
                popped = stack.pop()
                if popped != "{":
                    return False
            elif(c == ")" and stack):
                popped = stack.pop()
                if popped != "(":
                    return False
            else:
                return False
        
        if not stack:
            return True
        
        return False