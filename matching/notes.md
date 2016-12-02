<h2> Template Matching </h2>

- **Relevant OpenCV Functions** : matchTemplate, usually combined with minMaxLoc
- Templates are effectively filters that we correlate / convolute with the underlying image to locate 'interesting' areas in the image 
- Generally returns the top left corner of the best matching box (bottom right in Octave / Matlab)
- Use with the normalized cross-correlation option for best results
- Normalized Cross-Correlation ensures that the filter kernel and image patch are normalized to have sigma = 1; to enable matching on similar scales
