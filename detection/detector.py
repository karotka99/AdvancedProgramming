import time
import cv2
import numpy
import imutils
from imutils.object_detection import non_max_suppression

descriptor = cv2.HOGDescriptor()
descriptor.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def apply_non_max_suppression(coordinates):
    coordinates = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in coordinates])
    return non_max_suppression(coordinates, probs=None, overlapThresh=0.6)


def detect(path: str):
    image = cv2.imread(path)
    smaller_image = imutils.resize(image, width=min(850, image.shape[1]))
    start = time.time()
    coordinates, weights = descriptor.detectMultiScale(smaller_image, winStride=(5, 7), padding=(18, 14), scale=1.2)
    coordinates = apply_non_max_suppression(coordinates)
    end = time.time()
    people = 0
    for i, (x, y, w, h) in enumerate(coordinates):
        if weights[i] > 0.2:
            cv2.rectangle(smaller_image, (x, y), (w, h), (20, 58, 240), 2)
            people += 1
    print(f'Number of People: {people}')
    print(f'Time of Detection: {(end - start):.4f}')
    return smaller_image


def print_result(image) -> None:
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
