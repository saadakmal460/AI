import pandas as pd
import numpy as np
import matplotlib.pylab as plt

np.random.seed(0)


# days = 365

# temperature = np.random.randint(10, 40, days)
# humidity = np.random.randint(30, 90, days)
# wind_speed = np.random.randint(0, 20, days)
# weather_condition = np.random.choice(['Sunny', 'Rainy', 'Cloudy'], days)

# weather_data_gen = pd.DataFrame({
#     'Date': pd.date_range(start='2023-01-01', periods=days, freq='D'),
#     'Temperature': temperature,
#     'Humidity': humidity,
#     'Wind Speed': wind_speed,
#     'Weather Condition': weather_condition
# })

# weather_data_gen.to_excel('weather_data.xlsx', index=False)

weather_data = pd.read_excel('weather_data.xlsx')

temp = weather_data['Temperature']

numpy_array = np.array(temp)

mean = np.mean(numpy_array)
median = np.median(numpy_array)
std = np.std(numpy_array)

print(f'Mean: {mean}')
print(f'Meadian: {median}')
print(f'Standard Deviation: {std}')


filtered = weather_data[(weather_data['Temperature'] > 30) & (weather_data['Weather Condition'] == 'Sunny')]
row_count = len(filtered)
print(f'Rows with temp > 30 and wether sunny: {row_count}')

grouped = weather_data.groupby('Weather Condition')
average_humidity = grouped['Humidity'].mean()
print(f'Average Humidity: {average_humidity}')

temperatures = weather_data['Temperature']
days = weather_data['Date']

temp_array = np.array(temperatures)
days_array = np.array(days)

plt.plot(days_array , temp_array)
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Temperature over the year")
plt.show()


weather_condition = weather_data.groupby('Weather Condition')['Weather Condition'].count()

conditions = weather_condition.index
counts = weather_condition.values

plt.bar(conditions, counts, color =['maroon' , 'blue' , 'green'])
plt.show()