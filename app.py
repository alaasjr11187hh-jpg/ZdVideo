import streamlit as st

st.title("ZadVideo - أداة تحليل وصناعة المحتوى")

video_url = st.text_input("قم بلصق رابط الفيديو هنا:")

if st.button("تحليل وبناء المحتوى"):
    if video_url:
        st.info("جاري فحص الرابط وتحليل المحتوى...")
        st.success("تم التحليل! يمكنك الآن البدء في صناعة محتواك.")
    else:
        st.warning("يرجى إدخال رابط صالح أولاً.")

