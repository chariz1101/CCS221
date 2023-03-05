import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title("This is Activity 1")

x1 = st.slider(
    'X1',
    0, 100)
st.write('Value of X1: ', x1)

y1 = st.slider(
    'Y1',
    0, 100)
st.write('Value of Y1: ', y1)

x2 = st.slider(
    'X2',
    0, 100)
st.write('Value of X2: ', x2)

y2 = st.slider(
    'Y2',
    0, 100)
st.write('Value of Y2: ', y2)

dx = y2 - x1
dy = y2 - y1

steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

Xinc = float(dx/steps)
Yinc = float(dy/steps)

for i in range(0, int(steps +1)):
    
    st.pyplot(int(x1), int(y1))
    x1 += Xinc
    y1 += Yinc

