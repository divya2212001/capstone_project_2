# password_strength_ai.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

# ==============================
# 1. Dataset
# ==============================
data = {
    "password": [
        "12345", "password", "qwerty",
        "Pass@123", "Strong#456", "Hello@2024",
        "Admin", "letmein", "Secure!789"
    ],
    "label": [0,0,0,1,1,1,0,0,1]  # 0 = weak, 1 = strong
}

df = pd.DataFrame(data)

# ==============================
# 2. Vectorization
# ==============================
vectorizer = CountVectorizer(analyzer='char')
X = vectorizer.fit_transform(df["password"])

# ==============================
# 3. Model
# ==============================
model = RandomForestClassifier()
model.fit(X, df["label"])

# ==============================
# 4. Prediction
# ==============================
def check_strength(pwd):
    vec = vectorizer.transform([pwd])
    pred = model.predict(vec)[0]
    return pred

# ==============================
# 5. Interactive
# ==============================
print("\n🔐 Password Strength Checker\n")

while True:
    pwd = input("Enter password: ")

    if pwd.lower() == "exit":
        break

    result = check_strength(pwd)

    if result == 1:
        print("💪 Strong Password\n")
    else:
        print("⚠️ Weak Password\n")