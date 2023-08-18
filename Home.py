import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import io
import base64

st.set_page_config(
    page_title="Fikz Portofolio",
    page_icon="🏠",
    layout="wide"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def resize_image(input_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    aspect_ratio = width / height
    new_height = size
    new_width = int(new_height * aspect_ratio)
    resized_image = original_image.resize((new_width, new_height))
    return resized_image

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/7c7dcfc4-e9bc-4f77-b66a-17aae5f24802/d1mFNJG9HF.json")


# ---- HEADER SECTION ----
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<h2 style="font-size: 45px;">Hi, I am Fikri 👋</h2>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-size: 35px;">A Data Enthusiast</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: justify;'>
        Dedicated and results-driven Data Analyst with a strong background in campus laboratory assistance, comprehensive data analyst training, 
        and impactful internship experiences. Armed with a keen eye for detail and a deep appreciation for the power of data, I am adept at harnessing 
        various analytical tools, including Python, Tableau, Google Spreadsheet, MS Excel, and SQL, to transform complex datasets into actionable insights. 
        My journey from hands-on laboratory work to rigorous training programs has honed my ability to identify patterns, solve problems, and communicate findings effectively. 
        I thrive on translating data into tangible solutions, and I am excited to contribute my skills to unlocking new opportunities and driving informed decision-making.

        Key Proficiencies: Data Analysis | Python | Tableau | Google Spreadsheet | MS Excel | SQL

        Let's connect and explore how I can bring my analytical expertise to help your team excel. 
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<h2 style="font-size: 20px;">Done forget to check the sidebar > for my portofolio </h2>', unsafe_allow_html=True)
    with col2:
        st.title(" ")
    with col3:
        st.title(" ")
        st.title(" ")
        resized_image = resize_image("images/foto.png", 300)
        st.image(resized_image)



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Work Experience")
        st.markdown('<h2 style="font-size: 20px;">Data Analyst Intern - Campaign.com    |  Jakarta, Indonesia  |   May 2022 - September 2022</h2>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Collecting app traffic data from Google Firebase, Google Play Console, and App Store Connect</li>
            <li>Clean data from duplicate value (users, install dates, etc)</li>
            <li>Analyzing data using Ms. Excel, and Spreadsheets</li>
            <li>Creating data visualization using Google Slides and Google Data Studio</li>
            <li>Create data analytical report</li>
            <li>Present the report to other team that related to data team</li>
        </ul>
        """, unsafe_allow_html=True)

        st.markdown('<h2 style="font-size: 20px;">Data Analyst Trainee - Brainnest    |   Bremen,Germany (Remote)  |   June 2022 - July 2022</h2>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Data gathering using Survey Monkey</li>
            <li>Create graphs and data related tables using SPSS</li>
            <li>Calculate correlation between data with SPSS</li>
            <li>Learn basic data gathering using SQL</li>
            <li>Create data analytical report using real data</li>
        </ul>
        """, unsafe_allow_html=True)

    with right_column:
        st_lottie(lottie_coding, height=450, key="coding")


with st.container():
    st.write("---")
    left_column, center_column, right_column = st.columns(3)
    with left_column:
        st.header("Education")
        st.markdown('<h2 style="font-size: 30spx;">Telkom University</h2>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 20px;">Bachelor Degree in Computer Engineering, GPA = 3.71</p>', unsafe_allow_html=True)
    with center_column:
        st.title(" ")
    with right_column:
        image = Image.open("images\logotelu.png")
        resized_image = image.resize((160,160))
        buffered = io.BytesIO()
        resized_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(f'<img src="data:image/png;base64,{img_str}" style="margin-left: 80px;">', unsafe_allow_html=True)

st.write("---")
st.markdown('<h2 style="font-size: 30px;">Find Out More</h2>', unsafe_allow_html=True)
st.write("[LinkedIn >](https://www.linkedin.com/in/fikri-putra-hidayat-341625224/)")
st.write("[Github >](https://github.com/ApolloFikz13)")
st.write("[Resume >](https://drive.google.com/file/d/1NFSAN0CN-y_JX_eALg28mczja9e6qoJD/view?usp=sharing)")
st.write("#")
st.markdown('<h2 style="font-size: 30px;">Done forget to check the sidebar > for my portofolio </h2>', unsafe_allow_html=True)