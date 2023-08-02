import streamlit as st
from parsing import parser

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Article summariser :)</h1>", unsafe_allow_html=True)
rss_feed = st.text_input('Enter RSS feed')
rss_feed_links = parser(rss_feed)

if rss_feed_links:
        for i, link in enumerate(rss_feed_links, 1):
            st.markdown(f"{i}. {link.strip()}", unsafe_allow_html=True)