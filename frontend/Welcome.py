import streamlit as st

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1543353071-873f17a7a088?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.write('<h1 style="color: black;">Welcome to Mitahar!</h1>', unsafe_allow_html=True)

st.sidebar.title("Please select a plan")
st.sidebar.write("From the plans given above")
