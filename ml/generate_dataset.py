
import pandas as pd
import numpy as np

np.random.seed(42)

rows = 300

data = {
    "files_changed": np.random.randint(1, 16, rows),
    "lines_changed": np.random.randint(10, 600, rows),
    "tests_touched": np.random.randint(0, 12, rows),
    "hour": np.random.randint(0, 24, rows)
}

df = pd.DataFrame(data)

# Generate failure labels using synthetic risk conditions
risk = (
    (df["files_changed"] > 8).astype(int) +
    (df["lines_changed"] > 300).astype(int) +
    (df["tests_touched"] == 0).astype(int) +
    (df["hour"] >= 22).astype(int)
)

df["failed"] = (risk >= 2).astype(int)

df.to_csv("ml/builds.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nBuild failure distribution:")
print(df["failed"].value_counts())
