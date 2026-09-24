import pandas as pd
import numpy as np

# Read CSV file
df = pd.read_csv(r"D:\26MCS32\student_performance.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Display basic information
print(df.head())

print(df.info())

print("Shape:", df.shape)

print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# Display available column names
print("\nColumn names:")
print(df.columns.tolist())

# Check certifications column
if "certifications_count" in df.columns:
    print("\nCertifications Count:")
    print(df["certifications_count"].value_counts())

else:
    print("\n'certifications_count' column not found.")

# Remote ratio
if "remote_ratio" in df.columns:

    remote_ratio = df["remote_ratio"].dropna().to_numpy()

    print("\nMean Result:", np.mean(remote_ratio))

    print("Median Result:", np.median(remote_ratio))

    print("Maximum Result:", np.max(remote_ratio))

    print("Minimum Result:", np.min(remote_ratio))

    # Find remote_ratio values greater than 1
    print("\nRows where remote_ratio > 1:")
    print(df[df["remote_ratio"] > 1])

else:
    print("\n'remote_ratio' column not found.")


# Group by certifications_count
if "certifications_count" in df.columns and "remote_ratio" in df.columns:

    print("\nAverage remote ratio by certifications count:")
    print(df.groupby("certifications_count")["remote_ratio"].mean())