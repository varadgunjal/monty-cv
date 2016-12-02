def haarCascadeClassifier(input_file):
    image = cv2.imread(input_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # default parameter values taken from pyimagesearch blog post
    rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7,
	                    minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

    return rects