import pandas as pd
import os
df = pd.read_excel("data/my_data.xlsx")

df = df.dropna()


os.makedirs("artifacts", exist_ok=True)

df.to_excel("artifacts/processed.xlsx", index=False)
print("Data preprocessing completed")