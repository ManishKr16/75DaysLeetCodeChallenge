class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        # Mapping of digits to letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_combination):
            # Base case: if the current combination is complete
            if len(current_combination) == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get the letters that the current digit maps to
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Loop through the letters and recurse
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop() # Backtrack
                
        backtrack(0, [])
        return result
        