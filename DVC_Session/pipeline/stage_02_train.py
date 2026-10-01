import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_excel("artifacts/processed.xlsx")

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

joblib.dump(model,"D:\\deployment_mlops\\DVC_session\\artifacts\\model.pkl")
    
print("Model trained successfully")