import pandas as pd
import numpy as np
import matplotlib.pylab as plt

np.random.seed(0)


# rows = 1000

# date_range = pd.date_range(start='2022-01-01', end='2024-09-30', freq='D')


# companies = ['Apple' , 'Amazon' , 'Google' , 'Microsoft' , 'Meta']

# dates = np.random.choice(date_range, rows , replace=False)
# companies = np.random.choice(companies , rows)
# open_price = np.random.randint(50, 500, rows)
# closed_price = np.random.randint(50, 500, rows)
# volume_traded = np.random.randint(1000, 1000000., rows)




# stocks_data_gen = pd.DataFrame({
#     'date' : dates,
#     'company' : companies,
#     'open_price' : open_price,
#     'close_price' : closed_price,
#     'volume_traded' : volume_traded
    
# })

# stocks_data_gen.to_excel('stocks_data.xlsx', index=False)


stocks_data = pd.read_excel('stocks_data.xlsx')


close_price_arr = np.array(stocks_data['close_price'])

open_price_arr = np.array(stocks_data['open_price'])


sub = np.subtract(close_price_arr , open_price_arr)
div = np.divide(sub , open_price_arr)
rounded = np.round(div , decimals=2)
change = np.multiply(rounded,100)

print(f'Change in stocks {change}')


stock_increase = stocks_data[stocks_data['close_price'].diff() > 2]
print(f'Stock price increase {stock_increase}')


volume_traded = stocks_data.groupby('company')['volume_traded'].sum()
print(f'Stocks sold {volume_traded}')




filtered = stocks_data[stocks_data['company'] == 'Apple']

dates = filtered['date'].sort_values()

close_price = filtered['close_price']


plt.plot(dates , close_price , marker='o')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Close Price Over Time')
plt.show()


stocks_data['change'] = stocks_data.groupby('company')['close_price'].pct_change() * 100


avg_change = stocks_data.groupby('company')['change'].mean()


plt.bar(avg_change.index , avg_change.values)


plt.xlabel('Company')
plt.ylabel('Average Percentage Change in Close Price')
plt.title('Average Percentage Change in Close Price for Different Companies')

plt.show()