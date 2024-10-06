class Solution(object):
   def average(self, salary):
    min_sal = float('inf')
    max_sal = float('-inf')
    total = 0
    for sal in salary:
        min_sal = min(min_sal, sal)
        max_sal = max(max_sal, sal)
        total += sal
    
    total -= (min_sal + max_sal)
    return float(total) / (len(salary) - 2)
 