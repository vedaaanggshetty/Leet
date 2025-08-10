class Solution(object):
    def isValid(self, s):
        string = "abc"
        # if string in s:
        #     return True
        # return False


        # st = []
        # for c in s:
        #     st.append(c)
        #     if len(st) >= 3 and st[-3:] == ["a", "b", "c"]:
        #         st.pop()
        #         st.pop()
        #         st.pop()
        # return len(st) == 0

        while string in s:
            s = s.replace(string, "")
        return s == ""