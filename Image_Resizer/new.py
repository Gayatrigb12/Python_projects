import cv2  # OpenCV library for image processing
import os
from datetime import datetime

# === Load the Image ===
image_path = "Untitled.jpeg"
# image_path = input("Image path: ")
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if image is None:
    print("❌ Failed to load image. Please check the file path or format.")
    exit()

cv2.imshow("Original Image - Shiva", image)  # Display the original image

# === Get Resize Percentage from User ===
try:
    scale_percent = int(input("📏 Enter scale percent (e.g., 50 for 50%): "))
    if not (1 <= scale_percent <= 500):
        raise ValueError
except ValueError:
    print("❌ Invalid input! Please enter a number between 1 and 500.")
    exit()

# === Calculate New Dimensions ===
original_width = image.shape[1]
original_height = image.shape[0]
new_width = int(original_width * scale_percent / 100)
new_height = int(original_height * scale_percent / 100)
new_dim = (new_width, new_height)

# === Resize the Image ===
resized_image = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

# === Set Output Path and Generate Dynamic Filename ===
output_dir = r"D:\PYTHON\Python_POC\Python_projects\Image_Resizer\resized_images"
os.makedirs(output_dir, exist_ok=True)  # Create folder if it doesn't exist

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"resized_image_{timestamp}.jpg"
output_path = os.path.join(output_dir, filename)

# === Save the Resized Image ===
cv2.imwrite(output_path, resized_image)
print(f"✅ Image successfully saved at: {output_path}")

# === Display Resized Image ===
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
