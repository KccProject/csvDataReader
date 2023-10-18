import pandas as pd

df = pd.read_csv('data_new.csv')

sum_X = df['X'].sum()
y_values = {f'y{i}': df[f'y{i}'].sum() for i in range(1, 14)}

for key, value in y_values.items():
    if sum_X > value:
        print(f"X is greater than {key}")
    else:
        print(f"{key} is greater than X")
