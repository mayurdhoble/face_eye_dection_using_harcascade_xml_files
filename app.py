import cv2
import numpy as np
import streamlit as st

#st.header("Face & Eye dector using pretrained Cascade Classifiers with Open cv2")
def detect_faces_and_eyes(image):

  face_classifier = cv2.CascadeClassifier(r"C:\Users\dell\OneDrive\Documents\harcascade\Haarcascades\haarcascade_frontalface_default.xml")
  eye_classifier = cv2.CascadeClassifier(r"C:\Users\dell\OneDrive\Documents\harcascade\Haarcascades\haarcascade_eye.xml")
  img = cv2.imread(image)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  faces = face_classifier.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # Green for faces
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)  # Red for eyes

  st.image(img)

st.title("Face and Eye Detection App")
uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image_data = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    #we save the image with a temporary filename
    temp_filename = f"uploaded_image.{uploaded_file.name.split('.')[-1]}"
    cv2.imwrite(temp_filename, image)

    # Now use this temporary filename for cv2.imread
    processed_image = detect_faces_and_eyes(temp_filename)


