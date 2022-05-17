from asyncore import write
import requests
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

#CD into project directory, then 'streamlit run app.py'

st.set_page_config(page_title="Nicholas Squicciarini", page_icon=":floppy_disk:", layout="wide")

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
    left_column, right_column, middle_column= st.columns((2,2,1))
    with left_column:
        st.header("A Little About Me!")
        #st.write("##")
        st.write(
            """
            - Born and raised on Long Island, NY
            - Junior Volunteer Firefighter
            """
        )
    with left_column:
        st.header("Awards")
        st.write(
            """
            - Awarded King Clancy Award as a varsity player who best exemplified leadership on and off the field (2019)
            - Awarded Long Island Metro Lacrosse Foundation Most Valuable Goalie (2019)
            - Awarded Long Island All-Conference (2019)
            - Member of the Massapequa High School NYS Champion Lacrosse Team (2019)
            """
        )

    with right_column:
        st.header("Education")
        st.subheader("Stony Brook University")
        st.write(
            """
            - Bachelor of Science in Technological Systems Management With  a Specialization  in Computer Science
            - Expected Graduation May 2023
            - GPA: TBD
            - Men's Lacrosse Team
            """
        )
        st.write("[Stony Brook Men's Lacrosse Roster >](https://stonybrookathletics.com/sports/mens-lacrosse/roster/nick-squicciarini/7638)")

    with right_column:
        st.subheader("Long Island University")
        st.write(
            """
            -Bachelor of Science in Computer Science
            - September 2019- May 2021
            - GPA: 3.57
            - Men's Lacrosse Team
            """
        )
        st.write("[Long Island University Men's Lacrosse Roster >](https://www.liuathletics.com/sports/mens-lacrosse/roster/nick-squicciarini/1045)")
    
    with middle_column:
        st.header("Skills")
        st.write(
            """
            - MySQL                
            - Python               
            - Java   
            - Excel            
            - VBA    
            - Github
            - VS Code
            - Windows OS
            - Mac OSX
            """
        )
           
        
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
            Position: Student Software Developer (Volunteer)
            - Programming Language: Python || Libraries: PySimpleGUI and Pandas
            - The application provided ECLI Vibes counselors with an interactive window to submit client's information and be stored with Excel
            """
        )
        st.markdown("[Link to GitHub](https://github.com/squicciarini16/ecliVibes-Python)")

st.write("##")

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
            - Programming Language: Python || Libraries: Pandas, MatplotLib, and Wordcloud
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