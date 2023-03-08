import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("This is Activity 2")


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



#importing required libraries

import streamlit as st

import matplotlib.pyplot as plt

import numpy as np



#creating a sample array

a = np.random.normal(1, 1, size=50)
# a = np.array([[1, 1, 1]], size=5)

#specifying the figure to plot 

fig, x = plt.subplots()

x.hist(a, bins=10)



#plotting the figure

st.pyplot(fig)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)
Copy
