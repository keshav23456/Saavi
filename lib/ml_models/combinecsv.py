import pandas as pd

# Specify the paths of the three CSV files you want to combine
file1 = 'harassment.csv'
file2 = 'terms1.csv'
file3 = 'terms2.csv'
file4 = 'term3.csv'

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)

# Combine the DataFrames using pd.concat
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('all_data.csv', index=False)

print("CSV files have been combined successfully!")
