import streamlit as st
import random

# ตั้งค่า page
st.set_page_config(page_title="🎨 เกมทายสี", page_icon="🎨", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #FF5733;'>🎨 เกมทายสี 🎨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ทายสีที่โปรแกรมสุ่มจาก list สี!</p>", unsafe_allow_html=True)

# รายการสี
สี = ["แดง", "เขียว", "น้ำเงิน", "เหลือง", "ม่วง", "ส้ม"]

# สร้างสีลับและรอบใน session state
if 'สีลับ' not in st.session_state:
    st.session_state.สีลับ = random.choice(สี)
if 'รอบ' not in st.session_state:
    st.session_state.รอบ = 1

# เลือกสีจากผู้เล่น
ทาย = st.selectbox("เลือกสีของคุณ:", สี)

# ปุ่มทาย
if st.button("ทายเลย!"):
    if ทาย == st.session_state.สีลับ:
        # Emoji ใหญ่กลางจอ
        st.markdown("<h1 style='text-align: center; font-size:100px;'>🎉</h1>", unsafe_allow_html=True)
        st.success(f"ถูกต้อง! สีที่ถูกคือ **{st.session_state.สีลับ}**")
        # สุ่มสีใหม่และรีเซ็ตรอบ
        st.session_state.สีลับ = random.choice(สี)
        st.session_state.รอบ = 1
    else:
        st.markdown("<h1 style='text-align: center; font-size:100px;'>❌</h1>", unsafe_allow_html=True)
        st.error(f"ผิดแล้ว! สีที่ถูกคือ **{st.session_state.สีลับ}** 😅")
        st.session_state.รอบ += 1

# แสดงรอบปัจจุบัน
st.info(f"คุณอยู่ในรอบที่ {st.session_state.รอบ}")
