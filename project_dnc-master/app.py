# streamlit 라이브러리
# - Python을 손쉽게 웹사이트를 생성할 수 있는 라이브러리
# 기존에는 HTML, CSS

import streamlit as st

news_category = {
    "society": "사회",
    "politics": "정치",
    "economic": "경제",
    "foreign": "국제",
    "culture": "문화",
    "entertain": "연예",
    "sports": "스포츠",
    "digital": "IT",
}
st.set_page_config(
    page_title="뉴스 수집기",
    page_icon="./image/favicon_01.png"

)

st.title(":red[NEWS] COLLECTOR")
st.text("DAUM 뉴스를 수집합니다.")

with st.form(key="form"):
    category = st.text_input("카테고리 입력").strip()
    submitted = st.form_submit_button("수집 눌러라 앙카나")

    if submitted:
        st.write(category)