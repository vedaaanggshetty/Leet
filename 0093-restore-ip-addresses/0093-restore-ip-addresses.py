class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        def BT(st, p):
            if len(p) == 4:
                if len(s) == st:
                    res.append('.'.join(p))
                return 
            for i in range(1,4):
                if st + i > len(s):
                    break

                ss = s[st:st+i]
                if(len(ss)>1 and ss.startswith('0')or int(ss)>255):
                    continue
                BT(st+i, p + [ss])
        
        BT(0, [])
        return res