import streamlit as st

st.title("Airthematic Operation")
st.markdown("Please give the inputs")

st.sidebar.title("Select the operation")
st.sidebar.markdown("Selcet the options accordily:")

choice = st.sidebar.selectbox('Select',('Add','Mul'))
selected_status = st.sidebar.selectbox('select number',options=['2N','3N'])

if choice == 'Add':
    if selected_status == '2N':
        n1 = st.number_input("Number 1:")
        n2 = st.number_input("Number 2:")
        sum = n1 + n2
        st.success(sum)
elif selected_status == '3N':
        n1 = st.number_input("Number 1:")
        n2 = st.number_input("Number 2:")
        n3 = st.number_input("Number 3:")
        sum = n1 + n2 + n3
        st.success(sum)
if choice == 'Mul':
    if selected_status == '2N':
        n1 = st.number_input("Number 1:")
        n2 = st.number_input("Number 2:")
        mul = n1 * n2
        st.success(mul)
elif selected_status == '3N':
        n1 = st.number_input("Number 1:")
        n2 = st.number_input("Number 2:")
        n3 = st.number_input("Number 3:")
        mul = n1 * n2 * n3
        st.success(mul)
