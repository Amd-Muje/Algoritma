import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 1. Menghasilkan bilangan acak
X = np.random.randint(0, 101, 50).reshape(-1, 1)

# 2. Membuat label (0 jika <= 50, 1 jika > 50)
y = (X > 50).astype(int).ravel()

# 3. Membagi data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Melatih model Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# 5. Memprediksi data testing
y_pred = model.predict(X_test)

# 6. Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy * 100:.2f}%')