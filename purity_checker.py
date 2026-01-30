import pandas as pd

# 1. Create the data
lab_data = {
    "pH_Level": [7.2, 6.8, 7.5, 7.0],
    "Absorbance": [0.12, 0.15, 0.11, 0.13]
}

# 2. Build the DataFrame
df = pd.DataFrame(lab_data)

# 3. Try the 'head' and 'mean'
print("--- First 3 Rows ---")
print(df.head(3))

print("\n--- Average pH ---")
print(df["pH_Level"].mean())
