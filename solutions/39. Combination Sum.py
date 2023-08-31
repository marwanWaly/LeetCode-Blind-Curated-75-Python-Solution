class Solution:        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, cur, total):
            # if we reached a solution add it to the global res
            if total == target:
                res.append(cur.copy())
                return

            # if the total exceded the target so we didn't reach a valid solution
            if total > target or i == len(candidates):
                return
            
            # first option: take current candidates
            cur.append(candidates[i])
            backtracking(i, cur, total + candidates[i])

            # return back the cur before first option
            cur.pop()

            # second option: don't take current candidates
            backtracking(i + 1, cur, total)
        
        # start our operation
        backtracking(0, [], 0)
        return res
