# 8 kb
# 275 x 183

import cv2  # imported cv2 for resizing image
import cv2
import os
from datetime import datetime
# image = cv2.imread("Untitled.jpeg")  # taken input image
image = cv2.imread("Untitled.jpeg", cv2.IMREAD_COLOR)
if image is None:
    print("Failed to load image. Check the file path or format.")
    exit()

cv2.imshow("Shiva", image)  # here image with tile

scale_percent = int(input("Scale Percent: "))  # how much you want to scale
width = int(image.shape[1] * scale_percent / 100)  # acutal pixel * scale div by 100 to get new pixel
height = int(image.shape[0] * scale_percent / 100)  # shap is array function and 0 , 1 indcate position

dim = (width, height)  # in dim tuple is store for hight and width

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# interpolation=cv2.INTER_AREA: The interpolation method used for resizing.
# cv2.INTER_AREA is generally best for shrinking images as it uses pixel area
# relation and provides good results when reducing image size.


# Set target directory
output_dir = r"D:\PYTHON\Python_POC\Python_projects\Image_Resizer\resized_images"

# Generate a dynamic filename (e.g., with timestamp)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"resized_image_{timestamp}.jpg"

# Combine directory and filename
output_path = os.path.join(output_dir, filename)

# Save the image
cv2.imwrite(output_path, resized)

print(f"Image saved as: {output_path}")

# cv2.imwrite("D:/resized-image-50.jpg", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

