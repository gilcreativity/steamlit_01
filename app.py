import streamlit as st


with st.sidebar:
    st.image("https://static.wixstatic.com/media/4360de_5d12982365d74b2c8a19837c31c212ef~mv2.png/v1/fill/w_380,h_82,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/4360de_5d12982365d74b2c8a19837c31c212ef~mv2.png")
    st.title("Data Analysis")
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info("This application allows you to test an automated ML pipeline using Streamlit")

st.write("Hello world!")
