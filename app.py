import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="연애 상담소",
    page_icon="💌",
    layout="centered"
)

# 제목
st.title("💌 간단 연애 상담 앱")
st.write("고민을 적으면 간단한 조언을 해드려요!")

# 사용자 입력
user_input = st.text_area(
    "연애 고민을 입력하세요",
    placeholder="예: 좋아하는 사람이 있는데 먼저 연락해도 될까요?"
)

# 상담 답변 리스트
answers = [
    "조금 용기를 내서 솔직하게 표현해보는 것도 좋아요 😊",
    "상대방의 마음도 천천히 알아가는 게 중요해요 💖",
    "너무 조급해하지 말고 자연스럽게 다가가보세요 🌸",
    "자신감을 가지는 게 가장 중요해요 ✨",
    "진심은 결국 전달되는 경우가 많아요 💌",
    "상대방을 배려하는 대화가 좋은 관계를 만들어요 🙂",
]

# 버튼
if st.button("상담 받기"):
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요!")
    else:
        st.success("상담 결과")
        st.write(random.choice(answers))

        # 추가 공감 문구
        st.info("너무 걱정하지 말고 자신의 마음도 소중히 생각하세요 💙")

# 하단 문구
st.caption("Made with Streamlit")
