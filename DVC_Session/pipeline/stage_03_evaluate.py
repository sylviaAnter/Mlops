import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
df = pd.read_excel("artifacts/processed.xlsx")
X = df.drop("Price", axis=1)
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)
model = joblib.load("artifacts/model.pkl")
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
with open("artifacts/metrics.txt", "w") as f:
    f.write(f"MAE: {mae}")
    
print(f"MAE: {mae}")
print("Newwwwwwww")
print(f"Model MAE = {mae}")