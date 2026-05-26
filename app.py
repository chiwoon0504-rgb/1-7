import streamlit as st

# 제목
st.title("💖 연애 스타일 테스트")

# 설명
st.write("간단한 질문으로 나의 연애 스타일을 알아보세요!")

# 질문
q1 = st.radio(
    "데이트할 때 나는?",
    ["계획을 세운다", "즉흥적으로 한다"]
)

q2 = st.radio(
    "연락 스타일은?",
    ["자주 연락", "필요할 때만"]
)

# 결과 버튼
if st.button("결과 보기"):

    # 결과 로직
    if q1 == "계획을 세운다" and q2 == "자주 연락":
        result = "💌 당신은 다정하고 안정적인 연애 스타일!"
    
    elif q1 == "즉흥적으로 한다" and q2 == "필요할 때만":
        result = "🔥 자유로운 매력의 연애 스타일!"
    
    else:
        result = "✨ 균형 잡힌 현실적인 연애 스타일!"

    # 결과 출력
    st.success(result)
