from asyncore import write
import requests
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="NS Portfolio", page_icon=":floppy_disk:", layout="wide")

# Use local CSS
def local_css(styles):
    with open(styles) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/styles.css")

# ---- LOAD ASSETS 
img_contact_form = Image.open("images/rosterPicture.jpg")
img_lottie_animation = Image.open("images/inGamePicture.jpg")
ecliVibes = Image.open("images/ecliVibesIMG.png")
jupyterNotebookPNG = Image.open("images/jupyterNotebook.png")

# ---- HEADER SECTION 
with st.container():
    # st.header("Hey There!, I'm Nicholas Squicciarini :wave:")
    # st.write("##")
    image_column, text_column = st.columns((.5, 2))
    with image_column:
        st.image(img_contact_form,output_format = "auto")
    with text_column:
        st.write("##")
        st.write("##")
        st.title("Hey There, I'm Nicholas Squicciarini :wave:")
        st.subheader("Social Media Links:")
        st.caption(":iphone:(https://twitter.com/squixh416)")
        st.caption(":camera:(https://www.instagram.com/squixh/)")
        st.caption(":computer:(https://github.com/squicciarini16)")

# ---- A little about me 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("A Little About Me!")
        #st.write("##")
        st.write(
            """
            Junior year at Stony Brook University:
            - Studying Technological Systems Management with a specialization in Computer Science.
            - Programming: My SQL, Python, Java, and VBA.
            - Computer Operation: Windows OS, macOS, PowerPoint, Excel.
            - Student Athelete playing Lacrosse
            """
        )
        st.write("[Stony Brook Men's Lacrosse Roster >](https://stonybrookathletics.com/sports/mens-lacrosse/roster/nick-squicciarini/7638)")
  

# ---- PROJECTS ----

#----ECLI Vibes Project
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((.5, 2))
    with image_column:
        st.image(ecliVibes, width= None)
    with text_column:
        st.subheader("ECLI Vibes | Long Island, NY")
        st.write(
            """
            Position: Student Software Developer
            - Development of a mobile application for a non-profit organization
            - The mobile application gave ECLI Vibes the ability to make their surveys online rather than over the phone and provide immediate feedback / solutions to their users
            - Utilized File Maker Pro
            """
        )
        st.markdown("[Link to GitHub](https://github.com/squicciarini16/ecliVibes)")

#---- Shooting Analysis Project
with st.container():
    image_column, text_column = st.columns((.5, 2))
    with image_column:
        st.image(jupyterNotebookPNG)
    with text_column:
        st.subheader("Jupyter Notebook Analysis")
        st.write(
            """
            Imported a Mass Shooting CSV from 2018 & analyzed specific areas of the data
            - Pandas
            - Matplotlib
            - Wordcloud
            """
        )
        st.markdown("[Link to GitHub](https://github.com/squicciarini16/massShootingAnalysis)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/2f5e8e295fc62664cdb5d67a354c4677" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()