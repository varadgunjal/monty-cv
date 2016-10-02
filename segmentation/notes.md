<h1> Segmentation </h1>

- Mask is usually set with -
```python
mask = np.zeros(input_image.shape[:2], dtype="uint8")
```

<h2> Otsu's Method </h2>

- Works on images with fairly stark contrast between foreground and background


<h1> Blobs </h1>

- Generally computed on binary or thresholded images
- Blobs are used in all the same cases that contours could be used, except that blobs give more complete information about a region