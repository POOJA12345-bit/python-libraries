# Pandas Examples
# Author: Your Name

import pandas as pd

# Create DataFrame
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

# Basic analysis
print("Head:\n", df.head())
print("Describe:\n", df.describe())

# Filtering
high_marks = df[df["Marks"] > 80]
print("Students with Marks > 80:\n", high_marks)