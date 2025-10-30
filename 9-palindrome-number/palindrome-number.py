class Solution(object):

    def isPalindrome(self, x):
        # x = str(x)
        # return x == x[::-1]
        temp = x
        if x < 0:
            return False

        rev=0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        x = temp
        return x == rev

        # st = []
        # for i in range(x):
        #     if x[i] == x[-i-1]:
        #         st.append(i)
        #         return True
