import pandas as pd
import numpy as np

column_names = ['Movie_Name', 'Year', 'Genre', 'Rating', 'Revenue']

# Read the CSV file
df = pd.read_csv('../data/raw/movies.csv', names=column_names, encoding='utf-8')

print("=== ORIGINAL DATAFRAME ===")
print(df)
print("\n" + "="*50)

def calculate_total_revenue(dataframe):
    total_revenue = 0
    for rev in dataframe['Revenue']:
        item = rev.split()

        if len(item) ==2:
            value = float(item[0])

            if item[1].lower()=="million":
                value /= 1000
            
            total_revenue += value
    return total_revenue



print(f"Total Revenue: ${calculate_total_revenue(df):,.2f} billion")


with open('../data/processed/movies_revenue.txt', 'w') as file:
    file.write(f"Total Revenue: ${calculate_total_revenue(df):,.2f} billion")


