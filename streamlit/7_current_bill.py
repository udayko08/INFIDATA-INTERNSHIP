import datetime

import streamlit as st

customer_name = st.text_input("Enter the customer name:")
customer_Id = st.number_input("Enter the customer id")
units = st.number_input("Enter the units:")
if units <= 100:
    bill = 0
    st.write("No need to pay bill",bill)
elif units >= 100:
    bill=(units-100)*5
    st.write("The Required Rs",bill)
elif units >200:
    bill=(units-200)*10 +100*5
    st.write("The Required Rs",bill)
    st.success(units)