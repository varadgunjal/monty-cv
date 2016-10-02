<h1> Histograms </h1>

- **Relevant OpenCV Methods** : cv2.calcHist, cv2.equalizeHist
- One of the most important building blocks in basic computer science
- Used as feature descriptors, in thresholding (Otsu's method assumes bimodal grayscale histogram) and in other image processing techniques

- Capture frequency distribution of a set of data and these provide a meaningful way to do computer vision algorithms.

- Represents distribution of pixel intensities in image
- Enable interpretation of data without explicit information about the source

- **Unnormalized histograms** count the raw frequency of pixel values, a **normalized histogram** computes relatie frequency
- Normalized histograms are much more important in terms of using histograms for image matching and other processing

- Normally, grayscale histograms are normalized. For best results with normalizing color histograms, they are normalized after converting to YCrCb color space  as - 
```python
cv2.cvtColor(input_image, output_image, cv2.COLOR_BGR2YCrCb)
```

