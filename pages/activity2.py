import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("This is Activity 2")



two_d_arr = np.array([[800, 800, 800],
                      [800, 800, 800],
                      [800, 800, 800]])
    
x = []
y = []
replace = []
    
def fill(x, y, replace):
    
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            two_d_arr[x][y] = replace
            
    img = px.imshow(two_d_arr)
    img.set_clim([1,1000])
    plt.colorbar()
    img.show()
    st.pyplot(img)
    
        
    
def main():

    x = st.slider(
        'X',
        0, 2)
    st.write('Value of X: ', x)

    y = st.slider(
        'Y',
        0, 2)
    st.write('Value of Y: ', y)

    replace = st.slider(
        'Color',
        1, 1000)
    st.write('Color: ', replace)

    fill(x, y, replace)



if __name__ == '__main__':
    main()