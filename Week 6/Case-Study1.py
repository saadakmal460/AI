import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split



#1.2
np.random.seed(0)

rows = 1000

customer_id = [i for i in range(rows)]
gender_arr = ['Male' , 'Female']

age = np.random.randint(18,70,rows)
annual_income = np.random.randint(20000,120000,rows)
gender = np.random.choice(gender_arr , rows)

isPurchased = np.random.randint(0,2,rows)

# customer_data_gen = pd.DataFrame({
#     'customer_id' : customer_id,
#     'age' : age,
#     'gender' : gender,
#     'annual_income' : annual_income,
#     'purchased' : isPurchased
# })

# customer_data_gen.to_excel('customer_data.xlsx' , index=False)


customer_data = pd.read_excel('customer_data.xlsx')

#1.3
first_ten = customer_data.head(10)
print(f'First ten rows\n {first_ten}')
print(f'Null values\n {customer_data['annual_income'].isnull()}')

#1.4
customer_data['annual_income'].fillna(customer_data['annual_income'].median())
print(f'Filling null values\n {customer_data['annual_income']}')


#1.5
customer_data['gender_numerical'] = customer_data['gender'].map({'Male':0 , 'Female':1})
print(f'Converted data \n {customer_data}')

#1.6
customer_data['min_max_age'] = (customer_data['age'] - customer_data['age'].min()) / (customer_data['age'].max() - customer_data['age'].min())
customer_data['min_max_annual_income'] = (customer_data['annual_income'] - customer_data['annual_income'].min()) / (customer_data['annual_income'].max() - customer_data['annual_income'].min())

print(f'Normalized Ages :\n {customer_data['min_max_age']}')
print(f'Normalized Annual Income :\n {customer_data['min_max_annual_income']}')


#1.7
plt.hist(customer_data['age'])
plt.show()


plt.scatter(customer_data['age'] , customer_data['annual_income'])
plt.show()



#1.8
coorelation = customer_data[['age' , 'annual_income' , 'purchased']].corr()

print(f'Coorelation {coorelation}')


#1.9
customer_data['income_per_age'] = customer_data['annual_income'] / customer_data['age']

print(f'Income per age\n {customer_data['income_per_age']}')



#1.10
customer_data.drop('customer_id' , axis=1 , inplace=True)

print(f'Data after droped columns\n {customer_data}')


X_train, X_test = train_test_split(
  customer_data , random_state=104,test_size=0.20, shuffle=True)


print('X_train : ')
print(X_train.head())
 
print('')
print('X_test : ')
print(X_test.head())