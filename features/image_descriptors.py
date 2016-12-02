import numpy as np

def color_channel_statistics(input_file):
    image = cv2.imread(input_file)
    (means, devs) = cv2.meanStdDev(image)

    feature_vector = np.concatenate([means, devs]).flatten()
    return feature_vector

# def color_histograms(input_file):



