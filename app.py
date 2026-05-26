import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="미니 지렁이 게임",
    page_icon="🐍",
    layout="centered"
)

st.title("🐍 미니 지렁이 게임")

# 게임 크기
SIZE = 10

# 세션 상태 초기화
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]

if "food" not in st.session_state:
    st.session_state.food = (
        random.randint(0, SIZE - 1),
        random.randint(0, SIZE - 1)
    )

if "direction" not in st.session_state:
    st.session_state.direction = "RIGHT"

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 방향 버튼
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("⬆️"):
        st.session_state.direction = "UP"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️"):
        st.session_state.direction = "LEFT"

with col2:
    if st.button("⬇️"):
        st.session_state.direction = "DOWN"

with col3:
    if st.button("➡️"):
        st.session_state.direction = "RIGHT"

# 게임 로직
if not st.session_state.game_over:

    head_x, head_y = st.session_state.snake[0]

    if st.session_state.direction == "UP":
        head_x -= 1
    elif st.session_state.direction == "DOWN":
        head_x += 1
    elif st.session_state.direction == "LEFT":
        head_y -= 1
    elif st.session_state.direction == "RIGHT":
        head_y += 1

    new_head = (head_x, head_y)

    # 벽 충돌
    if (
        head_x < 0 or head_x >= SIZE or
        head_y < 0 or head_y >= SIZE
    ):
        st.session_state.game_over = True

    # 몸 충돌
    elif new_head in st.session_state.snake:
        st.session_state.game_over = True

    else:
        st.session_state.snake.insert(0, new_head)

        # 음식 먹기
        if new_head == st.session_state.food:
            st.session_state.food = (
                random.randint(0, SIZE - 1),
                random.randint(0, SIZE - 1)
            )
        else:
            st.session_state.snake.pop()

# 게임판 만들기
board = ""

for i in range(SIZE):
    for j in range(SIZE):

        if (i, j) == st.session_state.food:
            board += "🍎"

        elif (i, j) in st.session_state.snake:
            if (i, j) == st.session_state.snake[0]:
                board += "🐍"
            else:
                board += "🟩"

        else:
            board += "⬜"

    board += "\n"

st.text(board)

# 점수
st.write(f"점수: {len(st.session_state.snake) - 1}")

# 게임 오버
if st.session_state.game_over:
    st.error("💀 게임 오버!")

    if st.button("다시 시작"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (
            random.randint(0, SIZE - 1),
            random.randint(0, SIZE - 1)
        )
        st.session_state.direction = "RIGHT"
        st.session_state.game_over = False
        st.rerun()

# 자동 새로고침
time.sleep(0.3)
st.rerun()
