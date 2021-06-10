# Road-Lane-Line-Detection
Road Line Detection is a machine learning project which detects the edges of lane using the Probabilistic Hough Line Transformation.

**Libraries used:**
1. Opencv
2. Matplotlib
3. Numpy

**This project was done by breaking it into 3 major steps:**

**1.  Masking and Applying Region of Interest:**
    
    Download the required files,libraries and Read the image using opnecv (cv2).
    Matplotlib was used to display the image so the image was converted into RGB since the cv reads the image in BGR format.
    The value of height, width and channel of image was received using shape method.
    Hence then as per the received width and height, region of interest was declared.
    Lastly, mask every other background except Region of interest using fillPoly method.
    
**2. Edge Detection:**
   
    Canny Edge Detection Algorithm was used for detecting edges of the lanes present in the region of interesst we have initialized or declared above.
    So for canny edge detection, image was firstly converted into gray scale image using cvtColor method.
   
**3. Hough Line Detection:**
   
    Probabilistic Hough Line Detection was used to detect the shape of the line whose edges we had detected in above method.
    Hence, we join the detected line using **draw_the_Line** method.
