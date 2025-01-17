class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst=[0,1,1]
        sum=0
        if n==0:
            return 0

        if n==1:
            return 1
        if n==2:
            return 1
        for  i in  range(n-3):
            sum=lst[-1]+lst[-2]+lst[-3]
            print(sum)
            lst.append(sum)
        return lst[-1]+lst[-2]+lst[-3]

        