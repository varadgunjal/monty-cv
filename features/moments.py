# Shape Descriptors

def hu_moments(input_file, contour):
    # TODO : Assert that the input_file is binary
    
    image = cv2.imread(input_file)
    (x, y, w, h) = cv2.boundingRect(contour)
    roi = image[y:y + h, x:x + w]
    hu_feature_vector = cv2.HuMoments(cv2.moments(roi)).flatten()

    return hu_feature_vector