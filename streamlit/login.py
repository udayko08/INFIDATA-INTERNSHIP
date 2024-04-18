import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator import  Authenticate
from  yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader = SafeLoader)

authenticator = Authenticate(
    config['C']
)