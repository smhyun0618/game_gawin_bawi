
import random
import streamlit as st

# 화면 제목과 안내 문구
st.title("✌️ 가위바위보 게임")
st.write("컴퓨터와 가위바위보 대결을 해보세요!")
st.write("아래 버튼 중 하나를 선택하세요.")

# 가위바위보 목록
choices = ["가위", "바위", "보"]

# 버튼 3개를 나란히 배치
col1, col2, col3 = st.columns(3)

# 사용자의 선택
user = None

with col1:
    if st.button("✌️ 가위"):
        user = "가위"

with col2:
    if st.button("✊ 바위"):
        user = "바위"

with col3:
    if st.button("✋ 보"):
        user = "보"

# 컴퓨터와 대결
if user is not None:

    # 컴퓨터가 랜덤으로 선택
    computer = random.choice(choices)

    st.subheader("🎮 대결 결과")

    st.write(f"나의 선택: {user}")
    st.write(f"컴퓨터의 선택: {computer}")

    # 승리, 패배, 무승부 판정
    if user == computer:
        st.warning("🤝 무승부입니다!")

    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):

        st.success("🎉 축하합니다! 당신이 이겼습니다!")
        st.balloons()

    else:
        st.error("😢 아쉽네요! 컴퓨터가 이겼습니다.")
