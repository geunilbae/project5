import streamlit as st

# 사이드바에서 선택 상자 생성
page = st.sidebar.selectbox('Navigate', ['Select an option', 'Go to Site 1', 'Go to Site 2'])

# 첫 번째 메뉴 선택시 링크 제공
if page == 'Go to Site 1':
    st.write("You will be redirected to Site 1.")
    st.markdown('<a href="https://cheokcheok101py-3dfsncgsxm7qqz8tmaqt8y.streamlit.app/" target="_self">Click here to go to Site 1</a>', unsafe_allow_html=True)

# 두 번째 메뉴 선택시 링크 제공
elif page == 'Go to Site 2':
    st.write("You will be redirected to Site 2.")
    st.markdown('<a href="https://cheokcheok102py-ubq3swbcmet64wqnmtzvhp.streamlit.app/" target="_self">Click here to go to Site 2</a>', unsafe_allow_html=True)
