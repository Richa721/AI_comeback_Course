import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    'tenure': [1, 5, 10, 15, 20, 25],
    'monthly_bill': [100, 80, 60, 50, 40, 30],
    'churn': [1, 1, 1, 0, 0, 0]
})

X = data[['tenure', 'monthly_bill']]
y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
