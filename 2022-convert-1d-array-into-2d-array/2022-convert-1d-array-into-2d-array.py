class Solution(object):
    def construct2DArray(self, original, m, n):
       
      if m * n != len(original):
        return []
      
      ans = []
      
      for i in range(m):  #why because you are looping through the columns
      # and then appending those chunks as rows..
        ans.append(original[i*n : (i+1) * n])
      return ans

    