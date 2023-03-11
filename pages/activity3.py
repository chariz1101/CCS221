import streamlit as st
import numpy as np
import matplotlib as plt
from PIL import Image
#import cv2

#i = int(1)

#def translation(image, x, y):
#       m_translation_ = np.float32([[1, 0, x],
#                                   [0, 1, y],
#                                    [0, 0, 1]
#                                 ])
#        translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
#    
#        plt.axis('off')
 #       plt.imshow(translated_image)
#        plt.show()
#        st.pyplot (translated_image)

def load_image ():
      img = Image.open("image1")
      im.show()
       
   

   
#def image_ups ():
#      image_upload = st.file_uploader("Upload a PNG file", accept_multiple_files=True)
#      for image_uploads in image_upload:
#         bytes_data = image_uploads.read()
#         st.write("filename:", image_uploads.name)
 #        img = load_image(image_upload)
#         st.image(image1)
        
        
        
        
        
        
        
        
        
        
        
        
def main ():
    st.title ("Activity 3: Image Manipulator")
    Manipulation = ["Translation", "Rotation", "Scaling", "Shear", "Reflection"]
    choice = st.sidebar.selectbox("Manipulation", Manipulation)
    
    if choice == "Translation" :
        st.subheader ("Translation")
        image_ups ()
#        for i in range(1,4):
#            image = cv2.imread(str(i)+".PNG")
#            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#            cols, rows, dims = image.shape
#        
#            translation ()
    if choice == "Rotation" :
        st.subheader ("Rotation")
                      
    if choice == "Scaling" :
        st.subheader ("Scaling")
                      
    if choice == "Shear" :
        st.subheader ("Shear")
   

    if choice == "Reflection" :
        st.subheader ("Reflection")
         
    
if __name__ == '__main__' :
    main()
