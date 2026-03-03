# OpenCV Example
# Author: Your Name

import cv2

# Read image
img = cv2.imread("sample.png")

if img is not None:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found.")