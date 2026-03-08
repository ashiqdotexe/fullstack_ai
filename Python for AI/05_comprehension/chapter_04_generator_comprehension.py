"""

In Python, a generator comprehension is similar to a list comprehension, but instead of creating the entire list in memory, it returns a generator object that produces items lazily (on demand).

This makes it more memory-efficient for large datasets.

"""
sales = [5,4,7,10,3,20,14]
total_good_sales = sum(sale for sale in sales if sale>3)
print(total_good_sales)