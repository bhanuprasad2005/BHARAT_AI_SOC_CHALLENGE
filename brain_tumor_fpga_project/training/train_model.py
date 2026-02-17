import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

# -------------------------
# Parameters
# -------------------------
IMG_SIZE = 64
DATA_DIR = r"C:\Users\Dell\Desktop\brain_tumor_fpga_project\dataset"

# -------------------------
# Load Dataset
# -------------------------
def load_data():
    X = []
    y = []

    for label in ["yes", "no"]:
        folder_path = os.path.join(DATA_DIR, label)
        class_num = 1 if label == "yes" else 0

        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img / 255.0
            X.append(img)
            y.append(class_num)

    return np.array(X), np.array(y)

print("Loading data...")
X, y = load_data()
print("Dataset shape:", X.shape)

# -------------------------
# Train / Test Split
# -------------------------
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

print("Training samples:", len(X_train))
print("Validation samples:", len(X_val))
print("Test samples:", len(X_test))

# -------------------------
# Build Lightweight CNN
# -------------------------
model = models.Sequential()

model.add(layers.Conv2D(8, (3,3), activation='relu', input_shape=(64,64,3)))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(16, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# -------------------------
# Train Model
# -------------------------
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=20,
    batch_size=16
)

# -------------------------
# Evaluate
# -------------------------
loss, acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", acc)

# -------------------------
# Save Model
# -------------------------
model.save(r"C:\Users\Dell\Desktop\brain_tumor_fpga_project\models\brain_tumor_lightweight.h5")
print("Model saved successfully!")
