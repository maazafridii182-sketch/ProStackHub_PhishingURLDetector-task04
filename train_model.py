import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Training Dataset Setup (0 = Safe URL, 1 = Phishing URL)
data = [
    # Safe/Legitimate URLs
    [18, 0, 0, 1, 0, 0, 0],
    [22, 0, 0, 1, 0, 0, 0],
    [25, 0, 0, 1, 1, 0, 0],
    [19, 0, 0, 1, 0, 0, 0],
    [24, 0, 0, 1, 0, 0, 0],
    [28, 0, 0, 1, 1, 0, 0],
    [21, 0, 0, 1, 0, 0, 0],
    [30, 0, 0, 1, 1, 0, 0],
    
    # Phishing/Unsafe URLs
    [75, 1, 0, 0, 3, 1, 1],
    [60, 0, 1, 0, 0, 0, 1],
    [85, 1, 0, 0, 4, 1, 1],
    [68, 0, 0, 0, 2, 1, 1],
    [90, 1, 1, 0, 3, 1, 1],
    [55, 0, 0, 0, 3, 1, 1],
    [70, 0, 0, 0, 2, 1, 1],
    [80, 1, 0, 0, 3, 1, 1],
]

# Multiply dataset for proper pattern training
data = data * 25

columns = ['url_length', 'having_at_symbol', 'having_ip', 'has_https', 'subdomain_count', 'prefix_suffix', 'label']
df = pd.DataFrame(data, columns=columns)

# Features (X) aur Target (y)
X = df.drop('label', axis=1)
y = df['label']

# Data Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Random Forest Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Accuracy Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Training Success! Accuracy: {accuracy * 100:.2f}%")

# 4. Save Model to File
joblib.dump(model, 'phishing_model.pkl')
print("Saved trained model as 'phishing_model.pkl'")