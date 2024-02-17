import streamlit as st

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://github.com/ayush-sharma11/mitahar/blob/main/frontend/images/mitahar.png?raw=true");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.title("Please select a plan from the ones above")