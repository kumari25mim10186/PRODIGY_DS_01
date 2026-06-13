import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output directory
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/population_data.csv")

# Dataset Overview
print("\nDataset Information")
print("-" * 40)
print(df.head())

print("\nSummary Statistics")
print(df.describe())

# -------------------------
# Gender Distribution
# -------------------------
gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(8, 5))
gender_counts.plot(kind="bar")

plt.title("Gender Distribution", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("outputs/gender_bar_chart.png")
plt.show()

# -------------------------
# Age Distribution
# -------------------------
plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=8
)

plt.title("Age Distribution", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("outputs/age_histogram.png")
plt.show()

print("\nVisualizations saved successfully in outputs folder.")