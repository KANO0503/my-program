import streamlit as st
import google.generativeai as genai

# Google AI API 키 설정
GOOGLE_API_KEY = "AIzaSyChoQnEN21rHHC7VRHupn5kxz5tWT1wR3A"
genai.configure(api_key=GOOGLE_API_KEY)

# 생성 모델 초기화
model = genai.GenerativeModel('gemini-pro')

# Streamlit 애플리케이션 시작
st.title("냉장고를 부탁해 셰프봇")

# 사용자 입력 받기
user_input = st.text_input("재료 입력")
user_input = "\"" + user_input + "\"" + " 따옴표 안에 음식재료가 있다면 재료로 15분 내로 만들 수 있는 레시피를 알려줘 하지만 음식으로 사용할 수 없는 재료라면 \"잘못된 재료입니다\"라고만 응답해"

# '전송' 버튼 클릭 시 동작
if st.button("전송"):
    # 모델에 사용자 입력 전달하여 응답 생성
    response = model.generate_content(user_input)
    # 생성된 응답 출력
    response_text = response.candidates[0].content.parts[0].text
    st.write("모델 응답:", response_text)