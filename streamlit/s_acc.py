import streamlit as st
st.sidebar.title('welcome to SBI')
account_type=st.sidebar.selectbox('create account',options=[None,'create account'])
option=st.sidebar.selectbox('select opration',options=[None,'deposit','withdraw','display'])

st.title('online banking')

if (account_type=='create account'):
    name=st.text_input('name:')
    c_number=st.text_input('cid:')
    branch=st.text_input(' branch:')
    initial_amount=st.number_input('initial amount')

if (option=='deposit'):
    deposit=st.number_input('enter the amount to deposit')
    balance1=initial_amount + deposit
    st.write('updated balance after deposit:',balance1)

elif(option=='withdraw'):
    withdraw=st.number_input('enter the amount to withdraw')
    balance2=initial_amount-withdraw
    if initial_amount <= withdraw:
        st.write("blance after deposite",balance2)
    else:
        st.warning("Insufficent balance")
    st.write('updated balance after deposit:',balance2)
elif (option == 'display'):
    st.write('The name is:', name)
    st.write('The c_number is:', c_number)
    st.write('The branch is:', branch)
    st.write('The initail amount is:', initial_amount)