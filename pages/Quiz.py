import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

png = str(".png")
fig = plt.figure()
path = str("pages/")



def translation(Bx_old, By_old):
    
    #Translation
    m_translation_ = np.float32([[1, 0, Bx_old],
                                 [0, 1, By_old],
                                 [0, 0, 1]])
    
 
    image = cv2.imread("1.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = (image.shape[:2])

    translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)


def translation_new(Bx_new,By_new):
    
    #Translation
    m_translation_ = np.float32([[1, 0, Bx_new],
                                 [0, 1, By_new],
                                 [0, 0, 1]])
    
 
    image = cv2.imread("1.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = (image.shape[:2])

    translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)


def main () :
    
    Bx_old = []
    By_old = []
    Tx = []
    Ty = []

    st.title('Quiz')
    
    x = st.sidebar.slider(
        'Initial X',
        0, 1000)
    st.write('Value of X: ', Bx_old)

    y = st.sidebar.slider(
        'Initial Y',
        0, 1000)
    st.write('Value of Y: ', By_old)

    x = st.sidebar.slider(
        'Added X',
        0, 1000)
    st.write('Value of X: ', Tx)

    y = st.sidebar.slider(
        'Added Y',
        0, 1000)
    st.write('Value of Y: ', Ty)

    Bx_new = Bx_old + Tx
    By_new = By_old + Ty

    translation(Bx_old, By_old)
    translation_new(Bx_new, By_new)

    
if __name__ == '__main__':
    main()
