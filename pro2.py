import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv(r"D:\26MCS32\student_performance.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Display column names
print("Available columns:")
print(df.columns.tolist())

# Check for age column
if "age" in df.columns:
    Age = df["age"]

    print("\nAge values:")
    print(Age)

    print("\nMean Age:", np.mean(Age.dropna()))
    print("Median Age:", np.median(Age.dropna()))
    print("Maximum Age:", np.max(Age.dropna()))
    print("Minimum Age:", np.min(Age.dropna()))

else:
    print("\nError: 'age' column was not found.")