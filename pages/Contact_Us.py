import streamlit as st
from send_email import send_email
import pandas


topics_data = pandas.read_csv("topics.csv")

st.header("Contact Me")

with (st.form(key="contact_form")):
    user_email = st.text_input("Your e-mail address")
    topic = st.selectbox("Select topic", topics_data["topic"])
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: New email from {user_email}

Topic: {topic}
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()

    if button:
        send_email(message)
        st.info("Your e-mail was send")


