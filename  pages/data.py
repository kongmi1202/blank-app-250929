import streamlit as st
import numpy as np

st.set_page_config(page_title="음정 독보력 훈련", layout="centered")
st.title("음정 독보력 향상 앱")
st.markdown("""
랜덤으로 음정을 들려주고, 사용자가 음 이름을 맞추는 훈련 앱입니다. 
""")

# 음정 정보
notes = {
	"C": 261.63,
	"D": 293.66,
	"E": 329.63,
	"F": 349.23,
	"G": 392.00,
	"A": 440.00,
	"B": 493.88
}

# 랜덤 음정 선택
if "current_note" not in st.session_state:
	st.session_state.current_note = np.random.choice(list(notes.keys()))

st.subheader("1. 음정 듣기")
sample_rate = 44100
t = np.linspace(0, 1, sample_rate, endpoint=False)
freq = notes[st.session_state.current_note]
audio = np.sin(2 * np.pi * freq * t)
st.audio(audio, format="audio/wav", sample_rate=sample_rate)

st.subheader("2. 음 이름 맞추기")
user_answer = st.selectbox("어떤 음인가요?", list(notes.keys()))

if st.button("정답 확인"):
	if user_answer == st.session_state.current_note:
		st.success(f"정답! {user_answer} 입니다.")
		st.session_state.current_note = np.random.choice(list(notes.keys()))
	else:
		st.error("오답! 다시 들어보고 맞춰보세요.")
