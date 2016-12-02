import numpy as np
import cv2

def canny(input_file, sigma=0.33):
    """
    Auto Canny implementation taken from imutils package written by Adrian Rosebrock (Pyimagesearch)
    """

    image = cv2.imread(input_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Median is much less susceptible to noise than mean. And the threshold
    # value as a pixel value from the image itself makes a lot of sense. 
    threshold_value = np.median(image)

    lower_hysteresis_threshold = int(max(0, (1.0 - sigma) * threshold_value))
    upper_hysteresis_threshold = int(min(255, (1.0 + sigma) * threshold_value))

    edge_map = cv2.Canny(lower_hysteresis_threshold, upper_hysteresis_threshold)
    return edge_map
    
