import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt



png = str(".png")
fig = plt.figure()
path = str("pages/")

def translation(i):
    
    #Translation
    m_translation_ = np.float32([[1, 0, 1],
                                 [0, 1, 2],
                                 [0, 0, 1]])
    
 
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = (image.shape[:2])

    translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)

    
    
def rotation(i):
    angle = np.radians(10)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])
    
   
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = image.shape[:2]

    rotated_image = cv2.warpPerspective(image, m_rotation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(rotated_image)
    plt.show()
    st.pyplot(fig)
    
    
    
def scaling(i):
    m_scaling_ = np.float32([[1.5, 0, 0],
                             [0, 1.8, 0],
                             [0, 0, 1]])
    
   
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = image.shape[:2]

    scaled_image = cv2.warpPerspective(image, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_image)
    plt.show()
    st.pyplot(fig)
    
def shear(i):
    
    # Shearing
    m_shearing_ = np.float32([[1, 0.5, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    
    
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = image.shape[:2]

    sheared_image = cv2.warpPerspective(image, m_shearing_,(int(cols*1.5), int(rows*1.5)))
    plt.axis('off')
    plt.imshow(sheared_image)
    plt.show()
    st.pyplot(fig)

def reflection(i):
    image = cv2.imread(address + str(i) + jpg)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = image.shape[:2]
    
    m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]])
    
  

    reflected_image = cv2.warpPerspective(image, m_reflection_,(int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(reflected_image)
    plt.show()
    st.pyplot(fig)

def main () :
    i = st.slider('Choose Image [1, 2, 3]', 1, 3)
    
    st.write("Translation")
    translation(i)
    
    st.write("Rotation")
    rotation(i)
    
    st.write("Scale")
    scaling(i)
    
    st.write("Shear")
    shear(i)
    
    st.write("Reflection")
    reflection(i)
    
    
if __name__ == '__main__':
    main()
