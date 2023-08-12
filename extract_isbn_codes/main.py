import cv2
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
from io import BytesIO

def extract_isbn_codes(img):
    image = cv2.cvtColor(np.array(Image.open(BytesIO(img))), cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    test_img = Image.fromarray(np.array(image))
    test_img.save("C:/Users/cool laptop ni shawn/Downloads/test.png")

    try:
        return decode(image)[0].data.decode("utf-8")
    except:
        return None
