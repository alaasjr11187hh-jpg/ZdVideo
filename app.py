import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="ZadVideo - AI Editor", page_icon="✨", layout="centered")

# تنسيق العنوان
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>ZadVideo ✨</h1>
    <p style='text-align: center; font-size: 18px;'>أداة الذكاء الاصطناعي لتحليل وتحرير المحتوى</p>
    <hr>
""", unsafe_allow_html=True)

# واجهة الإدخال
video_url = st.text_input("🔗 الصق رابط الفيديو هنا", placeholder="https://youtube.com/...")

if st.button("تحليل الآن"):
    if video_url:
        with st.spinner('جاري معالجة الفيديو بواسطة الذكاء الاصطناعي...'):
            st.success("تم تحليل الفيديو بنجاح! 🚀")
            st.info("النتائج جاهزة للمراجعة.")
    else:
        st.error("يرجى التأكد من وضع رابط صحيح.")

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center;'>صُمم بواسطة ZadVideo - 2026</p>", unsafe_allow_html=True)

