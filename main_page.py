import streamlit as st
import webbrowser

# 사이드바에서 선택할 수 있는 옵션들
page = st.sidebar.selectbox(
    'Go to website',
    ['Select an option', 'Streamlit']
)

# 선택한 옵션에 따라 다른 URL로 이동
if page == 'Streamlit':
    webbrowser.open_new_tab('https://cheokcheok101py-3dfsncgsxm7qqz8tmaqt8y.streamlit.app/')
