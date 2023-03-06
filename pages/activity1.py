import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt



def DDALine(x1, y1, x2, y2, color):
    dx = y2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx/steps)
    Yinc = float(dy/steps)

    fig = plt.figure()  
    for i in range(0, int(steps +1)):
            
            plt.plot([int(x1), int(y1)])
            x1 += Xinc
            y1 += Yinc
            
    plt.show() 
    st.pyplot(fig)

        


def main(): 
    st.title("This is Activity 1")

    x = st.slider(
        'X1',
        0, 100)
    st.write('Value of X1: ', x)

    y = st.slider(
        'Y1',
        0, 100)
    st.write('Value of Y1: ', y)

    xEnd = st.slider(
        'X2',
        0, 100)
    st.write('Value of X2: ', xEnd)

    yEnd = st.slider(
        'Y2',
        0, 100)
    st.write('Value of Y2: ', yEnd)
    color = "b." 

    DDALine(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()    