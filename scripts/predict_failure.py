
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("ml/builds.csv")

# Separate features and target
X = df.drop(columns="failed")
y = df["failed"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Display feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(importance)

# Predict a large, untested, late-night commit
large_commit = pd.DataFrame([{
    "files_changed": 12,
    "lines_changed": 450,
    "tests_touched": 0,
    "hour": 22
}])

# Predict a small, well-tested change
small_commit = pd.DataFrame([{
    "files_changed": 2,
    "lines_changed": 30,
    "tests_touched": 5,
    "hour": 14
}])

large_risk = model.predict_proba(large_commit)[0][1]
small_risk = model.predict_proba(small_commit)[0][1]

print("\nBuild Failure Risk Predictions:")
print(f"Large commit failure risk: {large_risk:.2%}")
print(f"Small commit failure risk: {small_risk:.2%}")

# Save model
joblib.dump(model, "ml/build_failure_model.pkl")

print("\nModel saved successfully!")
