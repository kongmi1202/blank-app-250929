import streamlit as st
import numpy as np

st.set_page_config(page_title="Streamlit 음악 데모", layout="centered")

st.title("Streamlit 음악/오디오 기능 데모")
st.markdown("""
Streamlit에서 지원하는 음악 및 오디오 관련 기능을 소개합니다.
""")

# 1. 오디오 파일 재생 (URL)
st.subheader("오디오 파일 재생 (URL)")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 2. 오디오 파일 업로드 및 재생
st.subheader("오디오 파일 업로드 및 재생")
audio_file = st.file_uploader("오디오 파일을 업로드하세요", type=["mp3", "wav", "ogg"])
if audio_file is not None:
    st.audio(audio_file)

# 3. numpy 배열로 생성한 임시 오디오 재생 (WAV)
st.subheader("numpy 배열로 생성한 임시 오디오 재생 (WAV)")
sample_rate = 44100
t = np.linspace(0, 2, 2 * sample_rate, endpoint=False)
note = np.sin(2 * np.pi * 440 * t)  # 440Hz 사인파
st.audio(note, format="audio/wav", sample_rate=sample_rate)

# 4. 오디오 플레이어 UI 안내
st.info("오디오 플레이어는 mp3, wav, ogg 등 다양한 포맷을 지원합니다.")
