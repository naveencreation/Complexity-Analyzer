import streamlit as st
from streamlit_option_menu import option_menu
from front import show_front_page
from main import show_main_page
from math1 import show_complexity_page

st.set_page_config(page_title="Complexity Analyser", layout="wide", menu_items={
    'Get Help': 'https://www.example.com/help',
    'Report a bug': 'https://www.example.com/bug',
    'About': "This is a Streamlit app to visualize and analyze time/space complexities."
})

PAGES = {
    "Visualizer": show_front_page,
    "Math-Way":show_complexity_page,
    "Analyzer": show_main_page,
}


if "username" not in st.session_state:
    st.session_state.username = "User"  


with st.sidebar:
    selected = option_menu(
        menu_title=f"Welcome, {st.session_state.username}",
        options=list(PAGES.keys()),
        icons=[ "bi bi-graph-up", "bi bi-person", "bi bi-database-fill-gear", "bi bi-graph-up", ],
        menu_icon="bi bi-robot",
        default_index=0,
    )


page = PAGES[selected]
page()
