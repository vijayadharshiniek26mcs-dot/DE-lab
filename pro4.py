import pandas as pd

# Load the dataset
df = pd.read_csv(r"D:\26MCS32\student_performance.csv")

                                                                                                                                             

print("========== DATASET ==========")
print(df)

# 1. Display the structure of the dataset
print("\n========== DATASET INFORMATION ==========")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

# 2. Detect missing values
print("\n========== MISSING VALUES BY COLUMN ==========")
missing_count = df.isnull().sum()
print(missing_count)

# 3. Calculate missing-value percentage
print("\n========== MISSING VALUE PERCENTAGE ==========")
missing_percentage = (df.isnull().sum() / len(df)) * 100

for column in df.columns:
    print(column, ":", round(missing_percentage[column], 2), "%")

# 4. Calculate total missing values
total_missing = df.isnull().sum().sum()

print("\nTotal Missing Values :", total_missing)

# 5. Check duplicate records
duplicates = df.duplicated().sum()
print("Duplicate Records   :", duplicates)

# 6. Evaluate data quality
total_cells = df.shape[0] * df.shape[1]    
missing_ratio = (total_missing / total_cells) * 100

print("\n========== DATA QUALITY ==========")

if missing_ratio == 0 and duplicates == 0:
    print("Data Quality : Excellent")
elif missing_ratio <= 5 and duplicates <= 2:
    print("Data Quality : Good")
elif missing_ratio <= 20:
    print("Data Quality : Moderate")
else:
    print("Data Quality : Poor")

print("Missing Data Ratio :", round(missing_ratio, 2), "%")