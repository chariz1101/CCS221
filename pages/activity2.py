import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



st.title("This is Activity 2")

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3, c4 = st.columns((2, 1, 1, 1))

# two_d_arr = np.array([[800, 800, 800],
#                       [800, 800, 800],
#                       [800, 800, 800]])
    
# x = []
# y = []
# replace = []
    
# def fill(x, y, replace):
    
#     for i in range(len(two_d_arr)):
#         for j in range(len(two_d_arr[i])):
#             two_d_arr[x][y] = replace
            
#     img = plt.figure(two_d_arr)
#     img.set_clim([1,1000])
#     plt.colorbar()
#     plt.show()
#     st.pyplot(img)
    
        
    
# def main():

#     x = st.slider(
#         'X',
#         0, 2)
#     st.write('Value of X: ', x)

#     y = st.slider(
#         'Y',
#         0, 2)
#     st.write('Value of Y: ', y)

#     replace = st.slider(
#         'Color',
#         1, 1000)
#     st.write('Color: ', replace)

#     fill(x, y, replace)



# if __name__ == '__main__':
#     main()