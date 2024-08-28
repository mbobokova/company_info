import streamlit as st
import pandas

# PAGE SETTINGS
st.set_page_config(layout="wide")

df = pandas.read_csv("data.csv")

# HEAD
head_page = st.container()

with head_page:
    st.header("The Best Company")
    content = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    st.write(content)

# BODY
content_page = st.container()

with content_page:
    st.subheader("Our Team")
    col1, col2, col3 = st.columns(3)

    with col1:
        for index, row in df[:4].iterrows():
            st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
            st.write(row["role"])
            st.image("images/" + row["image"])

    with col2:
        for index, row in df[4:8].iterrows():
            st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
            st.write(row["role"])
            st.image("images/" + row["image"])

    with col3:
        for index, row in df[8:12].iterrows():
            st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
            st.write(row["role"])
            st.image("images/" + row["image"])
