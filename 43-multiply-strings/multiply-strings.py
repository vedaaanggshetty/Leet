class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1,num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                mul = (ord(num1[i]) -ord('0')) * (ord(num2[j])-ord('0'))
                summ = mul + res[i+j+1]
                res[i+j+1] = summ % 10
                res[i+j] += summ//10

        res = ''.join(map(str,res))
        return res.lstrip('0')
            



# forbidden usage
        # n1 = int(num1)
        # n2 = int(num2)
        
        # return str(n1 * n2)