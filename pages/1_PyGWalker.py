import streamlit as st
import pandas as pd
import plotly.express as px
import pygwalker as pyg

cp = pd.read_csv("pages/bitcoin.csv")
gwalker = pyg.walk(cp)

# Set page layout to wide
st.set_page_config(layout="wide")

st.write("---")
st.title("Bitcoin Data Analysis with PyGWalker Interactive Dashboard")

st.write("---")
st.subheader('Project Overview')
st.markdown("""
<p style='text-align: justify;'>
In this project, I will be building an interactive dashboard similar to Tableau using PyGWalker and Streamlit. The goal is to visualize and explore Bitcoin 
historical price data in an intuitive and interactive manner. By leveraging the capabilities of PyGWalker and the simplicity of Streamlit, we can create a 
user-friendly web app that allows users to interactively analyze and visualize the Bitcoin price data.
</p>
""", unsafe_allow_html=True)

st.write("---")
intro_text = """
### Introduction to PyGWalker

PyGWalker is a Python library that provides a Tableau-like UI for data exploration and visualization within Jupyter Notebook and other Jupyter-based environments. It simplifies the data analysis and visualization process by offering a no-code user interface for visual exploration. You can leverage dragging and dropping functionality to quickly create interactive visualizations without writing code.

Here are some key points about PyGWalker:

- PyGWalker is a Python binding of Graphic Walker, an open-source alternative to Tableau.
- It can take a Pandas, Polars, or Modin DataFrame and turn it into a visual exploration interface.
- PyGWalker is compatible with Jupyter Notebook, Jupyter Lab, Google Colab, Kaggle Code, Databricks Notebook, Visual Studio (with Jupyter Notebook extension), Hex Projects, IPython, and other Jupyter-based environments.
- It supports various environments, including Streamlit, Jupyter Extension for Visual Studio Code, and most web applications compatible with IPython kernels.
- PyGWalker can be installed using pip with the command pip install pygwalker. You can also use conda to install it with conda install -c conda-forge pygwalker.
- The library provides configuration options, such as privacy settings, that can be modified using the command line interface or through Python code.

Please note that PyGWalker may have specific use cases or limitations that are not covered in the available information. It's always a good idea to refer to the official documentation and examples provided by the library's creators for more detailed information on how to use PyGWalker in your projects.

"""
st.markdown(intro_text)
st.write("[Documentation >](https://docs.kanaries.net/pygwalker)")


st.write("---")
st.subheader("Bitcoin Data")
st.dataframe(cp)

st.write("---")
st.subheader("Correlation Matrix")
st.dataframe(cp.corr())

st.write("---")
st.subheader("Price Chart")
fig = px.line(cp, x="date", y="price")
st.plotly_chart(fig)

highest_price = cp['price'].max()
date_of_highest_price = cp['date'][cp['price'].idxmax()]
st.markdown(f"<h2 style='font-size: 20px;'>The highest price is: USD {highest_price}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2 style='font-size: 20px;'>The date of the highest price is: {date_of_highest_price}</h2>", unsafe_allow_html=True)

st.write("---")
st.subheader("PyGWalker Interactive Dashboard")
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
df = load_data("pages/bitcoin.csv")

# Display PyGWalker
def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config_str = config_file.read()
    return config_str
config = load_config('pages\config.json')
pyg.walk(df, env='Streamlit', dark='light', spec=config)