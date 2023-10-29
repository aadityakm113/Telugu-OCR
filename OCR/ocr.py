from PIL import Image
import pytesseract
import numpy as np
import cv2

img=cv2.imread('Images/telugu-text.png')
language='Telugu'
text = pytesseract.image_to_string(img, lang=language)
#print(img)

print(text)