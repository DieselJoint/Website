from PIL import Image
import requests
import streamlit as st
#Removed lottie import for streamlit as it was not returning the actual json file for the render

st.set_page_config(page_title="Nick's Webpage", layout="wide")


#also removed the function for calling lottie json url


#local_css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Website/style/style.css")
# -- Asset load

img_calc_form = Image.open("Website/images/Calculator.png")
img_dis_form = Image.open("Website/images/Discord.png")
# -- Header --
with st.container():
    st.subheader("Hi, my name is Nick")
    st.title("A self taught programmer")
    st.write("<p style='text-align: center;'> I am interested in learning how to program and build websites and more "
             "with "
             "different programming "
             "languages </p>", unsafe_allow_html=True)
# -- What I plan to do --
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I plan to do")
        st.write("##")
        st.write(
            """I plan to continue learning Python, JavaScript, HTML and CSS as well as other programming langauges 
            for software development""")

    with right_column:
            st.markdown("![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3J2b3ZnYXBnbnVud2t6NTNsc2MxNWpsdG41cWVxcWxvcTc1NDl0cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/coxQHKASG60HrHtvkt/giphy.webp)")

# -- Projects --
with st.container():
    st.write("---")
    st.header("Projects I'm working on")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_calc_form)
    with text_column:
        st.subheader("Executable Calculator Program")
        st.write(
            """I am Currently learning about GUI's and importing pip's such as flask and math functions""")

with st.container():
    text_column, image_column = st.columns((1, 2))
    with text_column:
        st.write("---")
        st.subheader("Discord bot")
        st.write(
            """Another project I'm currently working on is a bot for discord that uses their API. It can look and check weather with input locations""")
    with image_column:
        st.write("---")
        st.image(img_dis_form)

# -- contact --
with st.container():
    st.write("---")
    st.header("Send me a message if you'd like:blush:")
    st.write("##")
    #doc
    contact_form = """<form action="https://formsubmit.co/nicholas.klecknerMI04@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Enter your message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
