import cv2

def sobel_gradient(input_file, visualize=False):
    """
    Sobel Kernels
    G_x =  -1  0  1       G_y = -1 -2  1
           -2  0  2              0  0  0
           -1  0  1              1  2  1
    """
    
    image = cv2.imread(input_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Compute gradients along the X and Y axis, respectively
    g_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
    g_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

    if visualize:
        g_x = cv2.convertScaleAbs(g_x)
        g_y = cv2.convertScaleAbs(g_y)

        sobel_combined = cv2.addWeighted(g_x, 0.5, g_y, 0.5, 0)

        return g_x, g_y, sobel_combined