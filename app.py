import streamlit as st

# 1. إعدادات الصفحة والألوان (خلفية فاتحة وتصميم مريح)
st.set_page_config(page_title="Engineering Titans", page_icon="🎀", layout="centered")

# دالة لتنسيق الأزرار وجعلها تبدو احترافية باللون الوردي (شعار سرطان الثدي)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #e75480;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-size: 18px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #c93d6a;
        color: white;
    }
    h1, h2, h3 {
        color: #c93d6a;
        text-align: center;
    }
    .sub-text {
        text-align: center;
        font-style: italic;
        color: #555;
    }
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة الواجهات والتنقل باستخدام الـ Session State
if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def reset_pages():
    st.session_state.page = 1

# --- الواجهة الأولى (Page 1): الاسم والشعار الأساسي ---
if st.session_state.page == 1:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title("Engineering Titans 🚀")
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Next"):
        next_page()

# --- الواجهة الثانية (Page 2): معلومات المريض والشعار الرئيسي ---
elif st.session_state.page == 2:
    st.title("AI-Powered Mammogram Analysis for Early Breast Cancer Detection")
    st.write("---")
    
    # عرض صورة الفراشة والشريط الوردي في المنتصف
    st.image("https://i.imgur.com/vHqgZfN.jpeg", width=220)
    
    st.markdown("<p class='sub-text'>\"Like butterflies we flourish when we feel safe\"</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #e75480; font-size: 20px;'>Your health matters ❤️</h3>", unsafe_allow_html=True)
    st.write("---")
    
    # حقول إدخال بيانات المريض المطلوبة بالتصميم
    st.text_input("Patient Name")
    st.number_input("Patient Age", min_value=1, max_value=120, value=30)
    st.text_input("Phone Number")
    st.text_area("Medical History")
    
    st.write("")
    if st.button("Next"):
        next_page()

# --- الواجهة الثالثة (Page 3): رفع الصورة الطبية ---
elif st.session_state.page == 3:
    st.title("UPLOAD IMAGE (DICOM)")
    st.write("---")
    st.write("الرجاء رفع صورة الماموجرام الطبية بصيغة DICOM أو صيغة صور عادية للفحص:")
    
    # أداة رفع الملفات مع سهم الرفع الإيحائي للتحليل
    uploaded_file = st.file_uploader("UPLOAD IMAGE (DICOM) ↑", type=["dcm", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.success("تم رفع الصورة بنجاح! جاهز للتحليل بالذكاء الاصطناعي... ⏳")
        
    st.write("")
    if st.button("Next"):
        next_page()

# --- الواجهة الرابعة (Page 4): تصنيف الحالة (Classification) ---
elif st.session_state.page == 4:
    st.title("Analysis Results - Classification")
    st.write("---")
    
    st.markdown("<h3 style='text-align: left;'>Classification Results:</h3>", unsafe_allow_html=True)
    
    # عرض النتائج كبطاقات ملونة واضحة ومبهرة للدكتور
    col1, col2 = st.columns(2)
    with col1:
        st.success("✨ NORMAL")
    with col2:
        st.error("⚠️ ABNORMAL")
        
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Next"):
        next_page()

# --- الواجهة الخامسة والأخيرة (Page 5): خطورة الحالة والنوع (Severity) ---
elif st.session_state.page == 5:
    st.title("Analysis Results - Severity")
    st.write("---")
    
    st.markdown("<h3 style='text-align: left;'>Severity Assessment:</h3>", unsafe_allow_html=True)
    
    # عرض التصنيفات الثلاثة المطلوبة في الواجهة الأخيرة حسب ملف التصميم
    st.info("🟢 BENIGN (حميد)")
    st.warning("🟡 ABNORMAL (غير طبيعي)")
    st.error("🔴 MALIGNANT (خبيث)")
        
    st.write("---")
    if st.button("ابدأ من جديد (Reset)"):
        reset_pages()
