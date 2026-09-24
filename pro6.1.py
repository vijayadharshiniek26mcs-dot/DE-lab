import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\26MCS32\ai_ds_job_salaries_2026.csv")

# Display statical sum("Statistical Summary:")
print(df.describe())                                                                                     

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# ------------------------------------------------
# Histogram
# ------------------------------------------------

numeric_df.hist(figsize=(10, 8))

plt.suptitle("Histograms of Numerical Features")
plt.tight_layout()
plt.show()

# ------------------------------------------------
# Boxplot
# ------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(data=numeric_df)

plt.title("Boxplot of Numerical Features")
plt.xticks(rotation=45)
plt.show()

# ------------------------------------------------
# Correlation Heatmap
# ------------------------------------------------

plt.figure(figsize=(10, 6))

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,           
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

