import streamlit as st

# 사이드바에서 선택 상자 생성
page = st.sidebar.selectbox('Navigate', ['Select an option', 'Go to Site 1', 'Go to Site 2'])

# 첫 번째 메뉴 선택시 Site 1로 리디렉션
if page == 'Go to Site 1':
    js = "window.location.href = 'https://cheokcheok101py-3dfsncgsxm7qqz8tmaqt8y.streamlit.app/'"
    st.components.v1.html(f"<script>{js}</script>", height=0)

# 두 번째 메뉴 선택시 Site 2로 리디렉션
elif page == 'Go to Site 2':
    js = "window.location.href = 'https://cheokcheok102py-ubq3swbcmet64wqnmtzvhp.streamlit.app/'"
    st.components.v1.html(f"<script>{js}</script>", height=0)
