<h1> Contours </h1>

- **Relevant OpenCV Functions** : findContours, drawContours
- Contour detection is generally performed on binary images for better accuracy. Sometimes we get lazy and use grayscale images instead.
- The binary images are obtained by appropriate thresholding

- **Protip** : When drawing countours always style code as -
```python
for (i, c) in enumerate(cnts):
	cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Single Contour", clone)
	cv2.waitKey(0)
```

for convenience (Credits : Pyimagesearch)

- Using the cv2.CHAIN_APPROX_NONE flag, we would be storing every single (x, y)coordinate along the contour. This requires significantly more memory. By using cv2.CHAIN_APPROX_SIMPLE we compress our horizontal, vertical, and diagonal segments into only end-points we are able to reduce memory consumption significantly without any substantial loss in contour accuracy.


<h2> Properties </h2>

- **Centroid**
- **Aspect Ratio**
- **Solidity**
- **Extent**
- **Convex Hull**


<h2> Contour Approximation </h2>

- **Relevant OpenCV Functions** : cv2.approxPolyDP
- Represent a contour by a reduced set of points from the current set using <a href="https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm"> split-and-merge </a> algorithm
- Epsilon tolerance for approxPolyDP is specified as a fraction of the perimeter of the contour. Larger epsilon => more points discarded from original contour