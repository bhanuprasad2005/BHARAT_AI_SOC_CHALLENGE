import time
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model

# Load model
model = load_model(r"C:\Users\Dell\Desktop\brain_tumor_fpga_project\models\brain_tumor_lightweight.h5")

IMG_SIZE = 64
DATA_DIR = r"C:\Users\Dell\Desktop\brain_tumor_fpga_project\dataset"

# Load one image
def load_one_image():
    folder = os.path.join(DATA_DIR, "yes")
    img_name = os.listdir(folder)[0]
    img_path = os.path.join(folder, img_name)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Warm-up run
sample = load_one_image()
model.predict(sample)

# Timing test
N = 100
start = time.time()

for _ in range(N):
    model.predict(sample)

end = time.time()

avg_time = (end - start) / N
fps = 1 / avg_time

print("Average inference time per image (seconds):", avg_time)
print("Frames per second (FPS):", fps)
