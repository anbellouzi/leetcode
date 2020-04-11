"""
Restate: check if pair of open and closed characters match each other in a string.
Questions: Are there any letters? Are there any spaces? Can the string contain 1 character?
Assumptions: Multiple open and closed parentheses and nested characters.
Solutions: create a stack to hold all open characters, then check if next closed char matches last char in stack, 
            if yes remove char from stack and repeat process
Explain: Time efficiency o(n) -> loop over nums once and return a result
Tradeoff: Stack uses memory to store open chars, in longer senerio it can take a lot of time. 
Improvments: Implement a differnet data type to lower runtime and memory usage
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []      # will hold all chars
        for c in s:
            if c == "{" or c == "[" or c == '(': # append open chars to stack
                stack.append(c)
            else:
                if len(stack) == 0 or (not self.validPair(stack[-1], c)): # check if stack is empty or pair does not match
                    return False
                left = stack.pop() # pair match remove it from stack

        return len(stack) == 0      # return true if stack is empty 

    # helper function to check if left and right pairs match
    def validPair(self, left, right):
        return (left == "{" and right == "}") or (left == "(" and right == ")") or (left == "[" and right == "]")
            


if __name__ == "__main__":
    solution = Solution()
    
    print(solution.isValid("()"))       #true
    print(solution.isValid("{]"))       #false
    print(solution.isValid("{[]}"))     #true
