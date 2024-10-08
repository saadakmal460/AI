import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split



#2.2
np.random.seed(0)

rows = 1000

employee_id = [i for i in range(rows)]
gender_arr = ['Male' , 'Female']

age = np.random.randint(22,60,rows)
years_of_experience = np.random.randint(1,40,rows)

gender = np.random.choice(gender_arr , rows)
performance_rating = np.random.randint(1,6,rows)


# employee_data_gen = pd.DataFrame({
#     'employee_id' : employee_id,
#     'age' : age,
#     'gender' : gender,
#     'experience' : years_of_experience,
#     'performance_rating' : performance_rating
# })

# employee_data_gen.to_excel('employee_data.xlsx' , index=False)

employee_data = pd.read_excel('employee_data.xlsx')


#2.3
first_fifteen = employee_data.head(15)
print(f'First 15 rows \n {first_fifteen}')
print(f'Null values\n {employee_data.isnull()}')


#2.4
employee_data['experience'].fillna(employee_data['experience'].mean())
print(f'Filling null values {employee_data['experience']}')


#2.5
employee_data['numerical_gender'] = employee_data['gender'].map({'Male':0 , 'Female':1})
print(f'Numerical column of gender\n {employee_data['numerical_gender']}')


#2.6
outliers = np.where((employee_data['experience'] > 40))
print(f'Outliers\n {outliers}')


#2.7
employee_data['age_normalized'] = (employee_data['age'] - employee_data['age'].mean()) / employee_data['age'].std()
employee_data['experience_normalized'] = (employee_data['experience'] - employee_data['experience'].mean()) / employee_data['experience'].std()
print(f'Normalized Data\n {employee_data}')


#2.8
plt.boxplot(employee_data['age'])
plt.show()


plt.scatter(employee_data['experience'] , employee_data['performance_rating'])
plt.show()


#2.9
coorelation = employee_data[['age' , 'performance_rating' , 'experience']].corr()
print(f'Coorelation {coorelation}')


#2.10
employee_data['experience_per_age'] = employee_data['experience'] / employee_data['age']
print(f'Experience per age\n {employee_data['experience_per_age']}')


#2.11
employee_data.drop('employee_id' , axis=1 , inplace=True)

print(f'Data after droped columns\n {employee_data}')

X_train, X_test = train_test_split(
  employee_data , random_state=104,test_size=0.20, shuffle=True)

print('X_train : ')
print(X_train.head())
 
print('')
print('X_test : ')
print(X_test.head())