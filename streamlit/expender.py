import streamlit as st

st.bar_chart({1,5,2,6,9,10})

with st.expander("See explanation"):
    st.write("The chart shoes no collections of amounts")
    st.image("kiccha.jpg")