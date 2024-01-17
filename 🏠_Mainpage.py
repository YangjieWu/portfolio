import streamlit as st
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide") 

#sidebar
st.sidebar.success("Select a page above.")

# Add the badge to the sidebar
# with st.sidebar:
# components.html(linkedin_badge_html, height=200)

#main page
st.header("About Me",divider='rainbow')

col1, col2, col3 = st.columns([1.3 ,0.2, 1])

with col1:
    st.write(
    ' Hello everyone!\
        My name is Yangjie and I hail from the bustling city of Shanghai, China.\
        I am a data scientist. My expertise lies in machine learning, statistics, and data driven business consulting.\
        I have spent my student life in Canada and have had the opportunity to experience Japanese culture extensively, both in Kanto and Kansai.'
    +
    'When I am not crunching numbers and creating algorithms,\
        you can find me hiking in the forest, learning French, or cooking up a storm in my kitchen.\
        I also enjoy staying active by playing tennis and badminton in my local community.'
    +
    '**I believe the First Principle Theory **'
    )
    st.markdown("###### 😄 Nick Name: William!")
    st.markdown("###### 👉 Study: UBC")
    # st.markdown("#### 🇨🇳 Nationality: Chinese")
    st.markdown("###### 📍 Location: Osaka, JP")
    st.markdown("###### 🏄 Interest: Full Stack, Data Science, Product Management")
    st.markdown("###### 🟡 Favorite Color: Organge")
    st.markdown("###### 👀 Linkedin: https://www.linkedin.com/in/yangjiewu/")
    
    #st.divider()
    with open("src/CV_YangjieWu_20231208.pdf", "rb") as file:
        pdf_file = file.read()

    st.download_button(
        label="Download my :blue[resume]",
        data=pdf_file,
        file_name="resume",
        mime="application/pdf")

with col3:
    st.image("src/portrait.jpeg", width=360)

st.subheader("My :blue[skills] ⚒️",divider='rainbow') #,divider='rainbow'

def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

# x = st.slider("Select a value")
# st.markdown(f"# {x} squared is {x * x}")
