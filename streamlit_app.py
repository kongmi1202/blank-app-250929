import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit 기능 데모", layout="wide")

# 제목 및 텍스트
st.title("Streamlit 기능 올인원 데모")
st.header("헤더 예시")
st.subheader("서브헤더 예시")
st.text("텍스트 예시")
st.markdown("**마크다운** 지원 :sparkles:")
st.code("print('Hello, Streamlit!')", language="python")

# 알림, 경고, 에러
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")

# 데이터 표시
df = pd.DataFrame(np.random.randn(10, 5), columns=[f"col{i}" for i in range(5)])
st.dataframe(df)
st.table(df.head())
st.json({"Streamlit": "Awesome", "Version": "1.0"})

# 차트
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

# Matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df["col0"], label="col0")
ax.legend()
st.pyplot(fig)


# 입력 위젯
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")
option = st.selectbox("옵션 선택", ["A", "B", "C"])
multi = st.multiselect("여러 옵션 선택", ["X", "Y", "Z"])
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")
color = st.color_picker("색상 선택", "#00f900")
slider = st.slider("슬라이더", 0, 100, 50)
file = st.file_uploader("파일 업로드")

# 버튼
if st.button("버튼 클릭"):
    st.write(f"{name}님, 버튼을 클릭했습니다!")

# 폼
with st.form("my_form"):
    st.write("폼 내부")
    form_text = st.text_input("폼 텍스트 입력")
    submitted = st.form_submit_button("폼 제출")
    if submitted:
        st.write(f"폼 제출됨: {form_text}")

# 사이드바
st.sidebar.title("사이드바")
st.sidebar.radio("사이드바 라디오", ["1번", "2번", "3번"])

# 컬럼 레이아웃
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

# 탭
tab1, tab2 = st.tabs(["탭1", "탭2"])
with tab1:
    st.write("탭1 내용")
with tab2:
    st.write("탭2 내용")

# Expander
with st.expander("더보기"):
    st.write("숨겨진 내용")

# 미디어
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")
st.audio(np.random.randn(44100), format="audio/wav")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")

# 프로그레스바
import time
progress = st.progress(0)
for i in range(1, 101):
    progress.progress(i)
    time.sleep(0.01)

# 상태 표시
with st.spinner("로딩 중..."):
    time.sleep(1)
st.success("로딩 완료!")
