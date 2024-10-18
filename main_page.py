import streamlit as st

# 사이드바에서 선택 상자 생성
page = st.sidebar.selectbox('Navigate', ['Select an option', 'Go to Site 1', 'Go to Site 2'])

# 첫 번째 메뉴 선택시 Site 1로 리디렉션
if page == 'Go to Site 1':
    st.write("Redirecting to Site 1...")
    st.markdown(f"<meta http-equiv='refresh' content='0; url=https://cheokcheok101py-3dfsncgsxm7qqz8tmaqt8y.streamlit.app/'>", unsafe_allow_html=True)

# 두 번째 메뉴 선택시 Site 2로 리디렉션
elif page == 'Go to Site 2':
    st.write("Redirecting to Site 2...")
    st.markdown(f"<meta http-equiv='refresh' content='0; url=https://cheokcheok102py-ubq3swbcmet64wqnmtzvhp.streamlit.app/'>", unsafe_allow_html=True)
