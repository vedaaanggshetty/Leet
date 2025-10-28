class Solution(object):
    def myAtoi(self, s):
        import re
        # ss = re.findall(r'[a-zA-Z]+').s
        cc = s.lstrip()
        sign = 1

        if not cc:
            return 0

        if cc[0] == "+":
            sign = 1
            cc = cc[1:]
        elif cc[0] == "-":
            sign = -1 
            cc = cc[1:]

        res = 0
        for c in cc:
            if c.isdigit():
                res = res * 10 + int(c)
            else:
                break
        
        res *= sign

        MAXX = 2 ** 31 -1
        MINN = -2 ** 31

        if res > MAXX:
            return MAXX
        elif res < MINN:
            return MINN

        return res