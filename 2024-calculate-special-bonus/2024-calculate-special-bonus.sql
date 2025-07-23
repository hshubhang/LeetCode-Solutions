SELECT 
  employee_id,
  CASE 
    WHEN Employees.employee_id % 2 != 0 AND Employees.name NOT LIKE 'M%' THEN Employees.salary
    ELSE 0
  END AS bonus
FROM Employees
Order by employee_id;