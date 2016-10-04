<h1> Features </h1>

<h2> Feature Vector</h2>

- Enable us to quantify an image as a list of numbers

<h2> Image Descriptor </h2>
<h2> Feature Descriptor </h2>


<h1> Exploring Image Descriptors </h1>


<h2> Color Channel Statistics </h2>

- **Relevant OpenCV Methods** : <a href="http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#meanstddev">cv2.meanStdDev</a> (Note : Calculates mean, std deviation for all channels of image)
- **NumPy Tip** : Multi-dimensional matrices can be converted to single-dimensional ones by using <code> flatten </code>


<h2> Moments </h2>

- Image moments often quantify **shape**, **area** and **orientation** of objects in images
- Common moments : **mean**, **variance**, **std deviation**, **skew**, **kurtosis**
- Regular moments can be computed as 

<img src="./moments.png"/>

- Invariance in moments (to enable practical use in feature vectors) is achieved by making measurements relative to a base value viz. for translation invariance, measurements are made by calculating the centroid first and then subtracting it from the x, y coordinates being used

<img src="./translation_invariance.png"/>

- This is known as a **Relative Moment** - but they are not very robust practically

- As another example, scale invariance (for use in comparison between feature vectors) can be achieved by resizing all ROIs being compared to the same size so as to not be influenced by the object dimensions, <em> before calculating the moments</em>. But this destroys a lot of information about the object.


<h3> Hu Moments </h3>

- **Relevant OpenCV Methods** : cv2.HuMoments
- Image descriptor
- Generally computed on binary segmentation (preferred) or contour of object in the image
- 7 moments to characterize objects in image - built using relative moments
- **Protip** : Remember to calculate Hu Moments <em> only for the ROI containing the object in the image </em>

- Obviously, Hu Moments are not practically useful in real world applications


<h3> Zernike Moments </h3>

- **No Relevant OpenCV Methods, only available in the Mahotas package** : 
- More powerful / accurate / robust image descriptor than Hu Moments 
- Based on orthogonal functions : no redundancies between moments



<h3> Haralick Texture </h3>

- **No Relevant OpenCV Methods, only available in the Mahotas package** : mahotas.features.haralick
- 13-dimensional feature vector
- Statistics on Gray-Level Concurrence Matrix (GLCM) : counts the number of times a pair of adjacent pixel values (with order preserved) occur in an image
    - For completeness, this adjacency is tested in 4 directions resulting in 4 GLCM matrices
    - 13-d feature vector is calculated using each GLCM & then averaged out for rotation invariance

<h1> Exploring Feature Descriptors </h1>
