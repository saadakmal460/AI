import pandas as pd
import numpy as np
import matplotlib.pylab as plt

np.random.seed(0)


# rows = 500

# products_array = ['Tea' , 'Coffee' , 'Drink' , 'Sugar' , 'Cake' , 'Pizza' , 'Burger' , 'Pasta' , 'Shawarma' , 'Wrap']
# products = np.random.choice(products_array , rows)
# prices = np.random.randint(10, 1000, rows)
# quantity = np.random.randint(1, 20, rows)
# date_of_purchase = pd.date_range(start='2024-01-01', periods=rows)


# sales_data_gen = pd.DataFrame({
#     'products' : products,
#     'prices' : prices,
#     'quantity' : quantity,
#     'date_of_purchase' : date_of_purchase
# })

# sales_data_gen.to_excel('sales_data.xlsx', index=False)

sales_data = pd.read_excel('sales_data.xlsx')

prices = np.array(sales_data['prices'])
quantity = np.array(sales_data['quantity'])

total_sales = np.multiply(prices , quantity)
print(f'Total sales {total_sales}')

sales_data['total_sales'] = total_sales


greater_sales = sales_data[(sales_data['total_sales'] > 100)]
print(greater_sales)


total_quantity_sales = sales_data.groupby('products')['quantity'].sum()
print(total_quantity_sales)


plt.scatter(prices, quantity)
plt.show()


plt.hist(np.array(sales_data['total_sales']))
plt.show() 