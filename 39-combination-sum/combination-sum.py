class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        # explore path
        # check bounds
        # if fits then save the path ( keep adding the sum until target)
        # else discard path

        def BT(i, curr, total):

            if target == total:
                res.append(list(curr))
                return

            if i >= len(candidates) or total >= target:
                return 

            curr.append(candidates[i])
            BT(i, curr, total + candidates[i])
            curr.pop()

            BT(i+1, curr, total)

        BT(0, [], 0)
        return res