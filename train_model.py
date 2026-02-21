import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("data/crop_data.csv")

# Features (inputs)
X = data.drop('label', axis=1)

# Target (output)
y = data['label']

# Split dataset into training & testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Save trained model
pickle.dump(model, open("model/crop_model.pkl", "wb"))

print("✅ Model trained & saved successfully!")
