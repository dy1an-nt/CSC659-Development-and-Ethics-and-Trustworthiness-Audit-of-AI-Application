import csv
import io

sample_csv = """Name,Price,Category
Apple,1.50,Fruit
Banana,0.75,Fruit
Cherry,3.00,Fruit
Mango,2.25,Fruit
"""

reader = csv.DictReader(io.StringIO(sample_csv))
prices = [float(row['Price']) for row in reader]
avg = sum(prices) / len(prices)
print(f"Average Price: ${avg:.2f}")
