import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title('이미지 업로드 및 표시')

# 이미지 URL
image_url = 'https://i.imgur.com/7cBH3fu.png'

# URL에서 이미지 가져오기
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

# 이미지 표시
st.image(img, caption='Uploaded Image', use_column_width=True)