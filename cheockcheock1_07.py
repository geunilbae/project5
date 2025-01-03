import streamlit as st
import pandas as pd
import datetime
import backend as bd

# Frontend 기능 구현 시작 ---

# GitHub 정보가 있는지 확인하고 파일 업로드 객체를 출력
github_info_loaded = bd.load_env_info()

# appraisal.csv 파일 경로
file_path = "satisfaction/appraisal.csv"

# 1 프레임
# 보고서 타이틀
col1, col2 = st.columns([0.55,0.45])
with col1:
    st.markdown(
        "<p style='font-size:25px; font-weight:bold; color:#000000;'>만족도 결과 및 추첨 하기 🏆</p>",
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        "<div style='text-align:right;width:100%;'><p style='font-size:15px; font-weight:normal; color:#aaaaaa;margin-top:10px;'>by <b style='font-size:16px;color:#0099FF'>CheockCheock</b><b style='font-size:22px;color:#009999'>1</b> <b style='font-size:14px;'>prototype v.01</b></p></div>",
        unsafe_allow_html=True
    )

if github_info_loaded:
    # 데이터 로드 및 기본 정보 표시
    total_count, average_score, satisfaction_score_100, appraisal_data = bd.get_appraisal_data(file_path)
    if appraisal_data is not None:
        start_date, end_date = bd.get_date_range(appraisal_data)
        with st.expander("⭐ 만족도 평가 결과", expanded=True):
            col1 , col2, col3 = st.columns([0.3,0.3, 0.3])
            with col1:
                st.markdown(
                    f"<p style='font-size:22px; font-weight:bold; color:#999999;text-align:center;'>총 평가 건수:<br/><b style='color:#000000;font-size:28px;'>{total_count}건</b></p>",
                    unsafe_allow_html=True
                )
            with col2:
                st.markdown(
                    f"<p style='font-size:22px; font-weight:bold; color:#999999;text-align:center;'>평균 점수:<br/><b style='color:#000000;font-size:28px;'>{average_score:.2f}</b></p>",
                    unsafe_allow_html=True
                )
            with col3:
                st.markdown(
                    f"<p style='font-size:22px; font-weight:bold; color:#999999;text-align:center;'>만족도 점수:<br/><b style='color:#0000FF;font-size:28px;'>{satisfaction_score_100:.2f}점</b></p>",
                    unsafe_allow_html=True
                )
               # 시작일자와 종료일자를 설정

            if start_date and end_date:
                st.write(f"평가 등록 기간: {start_date.date()} ~ {end_date.date()}")
        if start_date and end_date:
            with st.expander("🏅 추첨 하기", expanded=False):
                col1 , col2 = st.columns([0.5,0.5])
                # 달력 입력창 추가
                with col1:
                    selected_start_date = st.date_input("시작일자 선택", value=start_date)
                with col2:
                    selected_end_date = st.date_input("종료일자 선택", value=end_date)
                    
                col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                with col1:
                    st.write("")
                with col2:
                    # [추첨하기] 버튼을 클릭하면, 기간 내 랜덤으로 1건 추출
                    if st.button("🎉 추첨하기",  use_container_width=True):
                        random_entry = bd.get_random_appraisal_in_range(appraisal_data, selected_start_date, selected_end_date)
                        if random_entry is not None:
                            col1, col2 = st.columns([0.6,0.4])
                            with col1:
                                st.markdown(
                                    f"<p style='font-size:20px; font-weight:bold; color:#000000;text-align:center;'>닉네임: <br/><b style='font-size:30px;color:#006666;'>{random_entry['ID']}</b></p>",
                                    unsafe_allow_html=True
                                )
                            with col2:
                                st.markdown(
                                    f"<p style='font-size:20px; font-weight:bold; color:#000000;text-align:center;'>날짜: <br/><b style='font-size:20px;'>{random_entry['DATE']}</b></p>",
                                    unsafe_allow_html=True
                                )
                            col1, col2, col3 = st.columns([0.05, 0.9, 0.05]) 
                            with col1:
                                st.write("")
                            with col2:
                                st.image("image/cheockcheock1_6.jpg",  use_column_width=True)
                            with col3:
                                st.write("")
                        else:
                            st.write("선택한 기간 내 데이터가 없습니다.")
                with col3:
                    st.write("")
                    

        with st.expander("📜 평가 내역 보기", expanded=False):
            # CSV 데이터를 HTML 테이블로 변환하여 표시
            html_table = bd.convert_data_to_html_table(appraisal_data)
            st.markdown(html_table, unsafe_allow_html=True)
    else:
        st.write("평가 데이터를 불러올 수 없습니다.")
else:
    st.warning("GitHub 정보가 설정되지 않았습니다. 먼저 GitHub Token을 입력해 주세요.")


