class Solution(object):
    def average(self, salary):
      sortedSal = sorted(salary)
      for i in range(len(sortedSal)):
       sorSal = sortedSal[1 : len(sortedSal)-1]
      average = float(sum(sorSal)) / len(sorSal)
      return float(average)