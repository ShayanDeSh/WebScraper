from keras.models import load_model
from imutils import paths
import numpy as np
import imutils
import cv2
import pickle


# def predict(image_file):
image_file = "captcha.jpeg"
with open("model_labels.dat", "rb") as f:
    lb = pickle.load(f)

model = load_model("captcha_model.hdf5")
image = cv2.imread(image_file)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('pr\\1' + '.jpeg', gray[0:40, 0:30])
cv2.imwrite('pr\\2' + '.jpeg', gray[0:40, 30:60])
cv2.imwrite('pr\\3' + '.jpeg', gray[0:40, 60:90])
cv2.imwrite('pr\\4' + '.jpeg', gray[0:40, 90:120])
cv2.imwrite('pr\\5' + '.jpeg', gray[0:40, 120:150])
letter = ''
for i in range(5):
    # img = mpimg.imread('pr\\' + (i + 1).__str__() + '.jpeg')
    # imgplot = plt.imshow(img)
    t = i + 1
    image1 = cv2.imread('pr\\' + t.__str__() + '.jpeg')
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image1 = cv2.resize(image1, (20, 20))
    image1 = np.expand_dims(image1, axis=2)
    image1 = np.expand_dims(image1, axis=0)
    prediction = model.predict(image1)
    letter = letter + lb.inverse_transform(prediction)[0]
print(letter)
# image1 = cv2.resize(gray, (20, 20))
# image1 = np.expand_dims(image1, axis=2)
# image1 = np.expand_dims(image1, axis=0)
# prediction = model.predict(image1)
# letter = lb.inverse_transform(prediction)[0]
# print(letter)
# print(letter)
