"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeeDict = {}
        for employee in employees:
            employeeDict[employee.id] = employee
        
        def dfs(employee_id):
            employee = employeeDict[employee_id]
            importanceSum = employee.importance
            for sub in employee.subordinates:
                importanceSum += dfs(sub)
            
            return importanceSum
        
        ans = dfs(id)
        return ans
        
