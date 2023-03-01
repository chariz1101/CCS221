import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("This is Activity 1")

x1 = st.slider(
    'X1',
    0.0, 100.0)
st.write('X1: ', x1)

y1 = st.slider(
    'Y1',
    0.0, 100.0)
st.write('Y1: ', y1)

x2 = st.slider(
    'X2',
    0.0, 100.0)
st.write('X2: ', x2)

y2 = st.slider(
    'Y2',
    0.0, 100.0)
st.write('Y2: ', y2)

color = "b." 
dx = y2 - x1
dy = y2 - y1

steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

Xinc = float(dx / steps)
Yinc = float(dy / steps)

for i in range(0, int(steps +1)):
    
    plt.plot(int(x1), int(y1), color)
    x1 += Xinc
    y1 += Yinc
    
plt.show()
    

# def main():
#     st.slider() = int(input("Enter X1: "))
#     st.slider() = int(input("Enter Y1: "))
#     xEnd = int(input("Enter X2: "))
#     yEnd = int(input("Enter Y2: "))
#     color = "b." 
#     DDALine(x, y, xEnd, yEnd, color)

# if __name__ == '__main__':
#     main()    