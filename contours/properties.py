import numpy as np
import cv2

def centroid(contour):
    M = cv2.moments(contour)
    centroid_x = int(M["m10"] / M["m00"])
    centroid_y = int(M["m01"] / M["m00"])

    return (centroid_x, centroid_y)    

def rotated_bounding_rect(contour):
    box = cv2.minAreaRect(c)    # returns ((x,y), (w, h), angle of rotation)
    box = np.int0(cv2.cv.BoxPoints(box))
    return box

# Bounding Rectangle, Circle, Ellipse have one-liner methods in OpenCV

def aspect_ratio(contour):
    (x, y, w, h) = cv2.boundingRect(contour)
    return w / float(h)

def extent(contour):
    contour_area = cv2.contourArea(contour)
    (x, y, w, h) = cv2.boundingRect(contour)

    bounding_rect_area = w * h

    return contour_area / float(bounding_rect_area)

def solidity(contour):
    contour_area = cv2.contourArea(contour)

    hull = cv2.convexHull(contour)
    hull_area = cv2.contourArea(hull)

    return contour_area / float(hull_area)

def approx_contour(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

    return approx