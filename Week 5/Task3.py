import pandas as pd
import numpy as np
import matplotlib.pylab as plt

np.random.seed(0)


rows = 300
names = ['Ahmed', 'Sarah', 'Ali', 'Fatima', 'Zain', 'Aisha', 'Omar', 'Noor', 'Hassan', 'Maria', 'Bilal', 'Zara', 'Saad', 'Sana', 'Imran', 'Layla', 'Usman', 'Hira', 'Yasir', 'Iman']
department = ['HR' , 'Marketing' , 'Finanace' , 'Development' , 'Sales']

employe_id = [i for i in range(rows)]

employee_names = np.random.choice(names , rows)
employee_department = np.random.choice(department , rows)

salary = np.random.randint(30000, 120000, rows)
experience = np.random.randint(1, 25, rows)



employee_data_gen = pd.DataFrame({
    'employee_id' : employe_id,
    'employe_name' : employee_names,
    'employee_department' : employee_department,
    'salary' : salary,
    'exprience' : experience
})

employee_data_gen.to_excel('employee_data.xlsx', index=False)

employee_data = pd.read_excel('employee_data.xlsx')

salary_array = np.array(employee_data['salary'])

average_salary = salary_array.mean()
max_salary = salary_array.max()
min_salary = salary_array.min()

print(f'Average salary: {average_salary}')
print(f'Max salary: {max_salary}')
print(f'Min salary: {min_salary}')


filtered_employees = employee_data[(employee_data['exprience'] > 5) & (employee_data['salary'] > average_salary)]
print(f'Filtered employees {filtered_employees}')


department_group = employee_data.groupby('employee_department')
department_salary_mean = department_group['salary'].mean()
print(f'Department mean salaries {department_salary_mean}')


plt.bar(department , department_salary_mean.values ,color =['red' , 'blue' , 'green' , 'yellow' , 'orange'])
plt.show()

salaries = np.array(employee_data['salary'])
exprience = np.array(employee_data['exprience'].sort_values())

plt.plot(exprience , salaries , marker='o')
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Experience with salaries")
plt.show()
