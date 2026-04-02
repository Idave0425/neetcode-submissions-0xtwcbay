class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, openN, closeN):
            if len(curr) == 2 * n:
                res.append(curr)
            
            if openN < n:
                backtrack(curr + "(", openN + 1, closeN)
            
            if closeN < openN:
                backtrack(curr + ")", openN, closeN + 1)
            
        
        backtrack("", 0, 0)

        return res
        