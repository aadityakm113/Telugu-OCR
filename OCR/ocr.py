from PIL import Image
from googletrans import Translator
from langdetect import detect_langs
import pytesseract
import numpy as np
import cv2


#function that carries out the OCR
def ocr(image):
    text = pytesseract.image_to_string(image, lang=language)
    return text

#Pre Processing the Image

#converts the image to grayscale
def greyscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#noise removal
def noise_rem(image):
    return cv2.medianBlur(image,5)

#thresholding
def thresh(image):
    return cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]

#normalization
def normalize(image):
    cv2norm_img = np.zeros((image.shape[0], image.shape[1]))
    return cv2.normalize(image, cv2norm_img, 0, 255, cv2.NORM_MINMAX)


img=cv2.imread('Images/telugu-text.png')
language='Telugu'

img=greyscale(img)
#img=noise_rem(img)
#img=thresh(img)
img=normalize(img)

text=ocr(img)
#test="hi my name is john. How are you?"
print(text)

translator=Translator()
#print(detect_langs(test))
tel_to_eng= translator.translate(text,dest='en')
print(tel_to_eng)





