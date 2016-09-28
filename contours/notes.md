<h1> Contours </h1>

- Contour detection is generally performed on binary images for better accuracy. At times, grayscale images are also used.

- **Protip** : When drawing countours always style code as 
```python
# loop over the contours individually and draw each of them
for (i, c) in enumerate(cnts):
	cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Single Contour", clone)
	cv2.waitKey(0)
```


- Using the cv2.CHAIN_APPROX_NONE flag, we would be storing every single (x, y)coordinate along the contour. This requires significantly more memory. By using cv2.CHAIN_APPROX_SIMPLE we compress our horizontal, vertical, and diagonal segments into only end-points we are able to reduce memory consumption significantly without any substantial loss in contour accuracy.


<h2> Properties </h2>

**Centroid**
- 