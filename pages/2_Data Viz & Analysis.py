import streamlit as st
import pandas as pd
import plotly.express as px
import pygwalker as pyg
import tempfile
import base64
from PIL import Image

def resize_image(input_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    aspect_ratio = width / height
    new_height = size
    new_width = int(new_height * aspect_ratio)
    resized_image = original_image.resize((new_width, new_height))
    return resized_image

st.set_page_config(layout="wide")

st.write("---")
st.title("Data Visualization and Analysis")

st.write("---")
st.subheader('Project Overview')
st.markdown("""
<p style='text-align: justify;'>
Welcome to a data-driven voyage where I fuse useful art data visualization with insightful analysis. My distinctive style merges creativity and precision, 
breathing life into complex datasets, and translating them into compelling visuals that resonate. Delving into data's depths, I uncover hidden patterns while 
keeping the broader context in sight, providing holistic insights for informed decisions. Crafting data analysis reports is an art in itself; my approach weaves clarity and usability into every word and visualization, 
presenting a harmonious narrative that guides readers through findings, analysis, and actionable conclusions. Get ready to experience a symphony of data where information takes form,
and insights are elegantly unveiled.
</p>
""", unsafe_allow_html=True)

st.write("---")
st.subheader('Data Visualization')
st.markdown(f"<h2 style='font-size: 20px;'>URL Search Console Data Visualization</h2>", unsafe_allow_html=True)

show_image = "images/Data URL Clicked dataviz.png"  
st.image(show_image, width=100, use_column_width=True)

st.write("---")
st.subheader('Data Analysis Report')
st.markdown("""
<p style='text-align: justify;'>
This data analysis report focuses on evaluating the financial status of a secondhand item company throughout the course of a year. The data is drawn from the company's warehouse inbound and outbound activities. 
The key financial metrics under examination include revenue, cost of goods sold (COGS), salary expenses, and delivery expenses. By analyzing this data, we aim to uncover insights into the company's financial performance, 
enabling informed decision-making to enhance its operations and profitability.
</p>
""", unsafe_allow_html=True)
st.write("[Take a look at the dataset >](https://docs.google.com/spreadsheets/d/1CeKmxVU5J_-sziIU5Rbdy4F5qAm5w-9hxFrfRGGw_Qg/edit?usp=sharing)")
col1, col2, col3 = st.columns(3)
with col2 :
    show_image = "images/6.png"  
    st.image(show_image, width=100, use_column_width=True)
    show_image = "images/7.png"  
    st.image(show_image, width=100, use_column_width=True)
    show_image = "images/8.png"  
    st.image(show_image, width=100, use_column_width=True)
    show_image = "images/9.png"  
    st.image(show_image, width=100, use_column_width=True)

st.write("---")
st.subheader('More Data Analysis')
st.markdown('<h2 style="font-size: 31px; text-align: center;">🙀 Sorry This Section is Under Development 😿</h2>', unsafe_allow_html=True)