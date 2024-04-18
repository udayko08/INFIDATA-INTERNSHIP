import streamlit as st

student_name = st.text_input("Enter the student name:")
student_reg = st.number_input("Enter the student regNo:")
grade = st.number_input("Enter the percentage")
if grade >90 and grade <=100:
    st.write("The Grade is A and percentage is",grade)
elif grade >80 and grade <=90:
    st.write("The Grade is B  and percentage is",grade)
elif grade >=60 and grade <=80:
    st.write("The Grade is C  and percentage is",grade)
elif grade <60:
    st.write("The Grade is D  and percentage is")