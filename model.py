import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("static/Crop_recommendation.csv")

# Features and target
X = data.iloc[:, :-1]  # all columns except last
y = data.iloc[:, -1]   # last column (label)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# If no 'season' column exists, skip get_dummies
# If season exists, encode it
if 'season' in X.columns:
    X_train = pd.get_dummies(X_train, columns=['season'], drop_first=True)
    X_test = pd.get_dummies(X_test, columns=['season'], drop_first=True)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")

# Save model and columns for use in app
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(list(X_train.columns), open("model_columns.pkl", "wb"))
