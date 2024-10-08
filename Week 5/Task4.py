import pandas as pd
import numpy as np
import matplotlib.pylab as plt

np.random.seed(0)


rows = 200
names = ['Ahmed', 'Sarah', 'Ali', 'Fatima', 'Zain', 'Aisha', 'Omar', 'Noor', 'Hassan', 'Maria', 'Bilal', 'Zara', 'Saad', 'Sana', 'Imran', 'Layla', 'Usman', 'Hira', 'Yasir', 'Iman']
subjects = ['PF' , 'TOA' , 'DE' , 'DM' , 'OOP']

# student_id = [i for i in range(rows)]
# student_names = np.random.choice(names , rows)
# subject = np.random.choice(subjects , rows)

# marks = np.random.randint(0, 100, rows)


# student_data_gen = pd.DataFrame({
#     'student_id' : student_id,
#     'name' : student_names,
#     'subject' : subject,
#     'marks' : marks,
# })

# student_data_gen.to_excel('student_data.xlsx', index=False)


student_data = pd.read_excel('student_data.xlsx')


student_marks = np.array(student_data['marks'])

mean = np.mean(student_marks)
median = np.median(student_marks)
# mode = student_marks.mode()
std = np.std(student_marks)


print(f'Mean: {mean}')
print(f'Meadian: {median}')
# print(f'Mode: {mode}')
print(f'Standard Deviation: {std}')



filtered_student = student_data[(student_data['marks'] > 80)]
print(f'Filtered students {filtered_student}')


subjects_mean = student_data.groupby('subject')['marks'].mean()

print(f'Subjects Mean {subjects_mean}')


plt.hist(np.array(student_data['marks']))
plt.show()


plt.bar(subjects_mean.index , subjects_mean.values , color =['red' , 'blue' , 'green' , 'yellow' , 'orange'])
plt.show()