import streamlit as st
import importlib

# 사이드바에서 페이지 선택
page = st.sidebar.selectbox('Navigate', ['Page 1'])

# 홈 페이지 처리
if page == 'Page 1':
    st.title("Page 1")
    page1 = importlib.import_module('cheokcheok1_01')
    page1.show()
