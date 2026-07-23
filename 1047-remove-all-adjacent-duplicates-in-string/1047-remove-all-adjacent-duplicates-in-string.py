class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            # If the stack has characters and the top character matches current,
            # pop it (remove adjacent pair)
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
                
        # Reconstruct the string from remaining characters in stack
        return "".join(stack)
        