class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only 1 row or not enough characters to fill rows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array of strings for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Step through the string character by character
        for char in s:
            rows[current_row] += char
            
            # Change direction if we land on the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move to the next row based on the direction
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)
        