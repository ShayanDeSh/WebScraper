import os
import pickle

import cv2
import numpy as np
from imutils import paths
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense

data = []
labels = []

for image_file in paths.list_images("let"):
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (20, 20))
    image = np.expand_dims(image, axis=2)
    label = image_file.split(os.path.sep)[-2]
    print(image_file)
    print(label)
    data.append(image)
    labels.append(label)
input()
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
Y_test = lb.transform(Y_test)

with open('model_labels.dat', "wb") as f:
    pickle.dump(lb, f)

model = Sequential()

model.add(Conv2D(20, (5, 5), padding="same", input_shape=(20, 20, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Flatten())
model.add(Dense(500, activation="relu"))

model.add(Dense(23, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=23, epochs=10, verbose=1)

model.save("captcha_model.hdf5")
