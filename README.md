***  Face and Eye Detection App with Streamlit and OpenCV  ***

This Streamlit application allows to upload an image and detect faces and eyes within it using OpenCV's pre-trained Haar cascade classifiers.

About OpenCV:

OpenCV (Open Source Computer Vision Library) is a powerful library for real-time computer vision applications. It provides a comprehensive set of functions for image processing, video analysis, and object detection. The library is widely used in various domains, including robotics, self-driving cars, and augmented reality.

Haar Cascade Classifiers:

OpenCV offers pre-trained Haar cascade classifiers for various object detection tasks, including faces and eyes. These classifiers are efficient and work well for real-time applications.

Functionality

The application performs the following steps:

Uploads an image using Streamlit's file_uploader widget.

Converts the uploaded image data to a NumPy array.

Uses OpenCV's cv2.cvtColor function to convert the image from BGR (OpenCV's default color format) to grayscale for better face detection.

Utilizes pre-trained Haar cascade classifiers for face and eye detection:

cv2.CascadeClassifier("haarcascade_frontalface_default.xml"): Detects frontal faces.

cv2.CascadeClassifier("haarcascade_eye.xml"): Detects eyes within the detected faces.

Draws green rectangles around detected faces and red rectangles around detected eyes on the original image.

Displays the processed image with detected features using Streamlit's st.image function.

Running the App:

Download the Haar cascade classifiers for face and eyes:
Click on link 
https://github.com/opencv/opencv/tree/master/data/haarcascades 

Place the downloaded XML files (e.g., haarcascade_frontalface_default.xml and haarcascade_eye.xml) in a folder accessible by script.

Update the file paths in the detect_faces_and_eyes function to point to the locations of downloaded XML files.

Run the script using Python (python app.py).

Disclaimer:

The provided file paths for the Haar cascade classifiers are for illustrative purposes. You will need to download and update them with the actual file paths on your system.
