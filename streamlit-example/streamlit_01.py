import streamlit as st

# Text/Title
st.title("OpenCampus")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("This is a text")

# markdown
st.markdown("### This is a markdown")

# Colorful text
st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error")
st.exception("NameError('name three not defined')")

# Get Help Info about Python
# Lets ask streamlit how range(works)
st.help(range)


# define custom fuction
def greet():
    """
    function to say hello
    """
    print("hello")


st.help(greet)

# write text/fctn
st.write(range(20))

# IMAGES
from PIL import Image
import requests
from io import BytesIO

# download and open image
url = "https://www.opencampus.it/wp-content/uploads/2021/01/ \
OC-gallery-or_0024_DSC05998-HDR-Pano.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# display image
st.image(img, width=500, caption="This is my cool caption")


# VIDEOS
vid_file = open("video-streamlit.mp4", "rb").read()
st.video(vid_file)


# AUSIO
audio_file = open("audio.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3")


# WIDGET
# checkbox
if st.checkbox("Show/Hide"):
    st.text("show or hide widget")

# radio
status = st.radio("What is your status?", ("Active", "Inactive"))

if status == "Active":
    st.success("You are active")
else:
    st.warning("Inactive")

# selectbox
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Doctor"])
st.write("You selected: ", occupation)

# multiselection
location = st.multiselect(
    "Where do you workd?", ("London", "New York", "Accra", "Kiev", "Nepal")
)

st.write("You selected: ", ", ".join(location))

# slider
st.slider("What is your Python level", 1, 10)

# buttons
if st.button("click here"):
    st.write("You clicked!")


# TEXT INPUT

# simple input
name = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
    st.write(name)

# multiple lines
message = st.text_area("Insert your long message here", "Type here...")
if st.button(
    "Submit", key="submit2"
):  # need to insert a key to differentiate from previous
    st.write(message)


# date input
import datetime

today = st.date_input("Today is ", datetime.datetime.now())
time_now = st.time_input("Insert time", datetime.time())

# display json
st.write("display json")
st.write({"name": "Marcello", "surname": "Politi"})

# display raw code
st.text("Display Raw Code")
st.code("import numpy as np")


# display raw code
with st.echo():
    [a for a in "ciao"]

# Progress Bar
import time

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text="progress_text")
time.sleep(1)
my_bar.empty()

st.button("Rerun")


# spinner
with st.spinner("Wait for it..."):
    time.sleep(3)
st.success("Done!")

# cool stuff
st.balloons()
st.snow()

# SIDEBARS
st.sidebar.header("Header")
st.sidebar.title("Title")
