class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for i in range(1, n):
            count = 1
            curr = ""

            for j in range(1, len(res)):
                if res[j] == res[j-1]:
                    count += 1
                else:
                    curr += str(count) + res[j-1]
                    count = 1
            curr += str(count) + res[-1]
            res = curr

        return res