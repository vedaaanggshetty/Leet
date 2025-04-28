class Solution(object):
    def letterCasePermutation(self, s):
        # res = [""]
        # for c in s:
        #     temp = []
        #     for r in res:
        #         if c.isalpha():
        #             temp.append(r + c.lower())
        #             temp.append(r + c.upper())
        #         else:
        #             temp.append(r + c)
        #     res = temp
        # return res

        #  BT
        res = []
        def BT(sub="",i=0):
            if(len(s)== len(sub)):
                res.append(sub)
                return 
            
            if(s[i].isalpha()):
                BT(sub + s[i].swapcase(), i+1)
            BT(sub + s[i], i+1)

        BT()
        return res