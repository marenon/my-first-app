import streamlit as st

# 1. إعدادات الصفحة لتكون متناسقة وثابتة بدون نزول بالواجهة
st.set_page_config(page_title="Engineering Titans", page_icon="🧬", layout="centered")

# دالة التنسيق الـ CSS المخصصة للخط والحجم والاتجاه والأزرار
st.markdown("""
    <style>
    /* تطبيق خط Al Dhabi وحجم 60 لجهة اليسار للعنوان الرئيسي */
    .custom-title {
        font-family: 'Al Dhabi', 'Segoe UI', sans-serif !important;
        font-size: 60px !important;
        color: #c93d6a;
        text-align: left !important;  /* جعل الكلام من جهة اليسار */
        font-weight: bold;
        margin-bottom: 5px !important;
        padding-left: 10px;
    }
    
    /* تغيير الخط لباقي عناصر الموقع ليكون احترافي ومودرن */
    html, body, [data-testid="stMarkdownContainer"], h2, h3, p, button, label {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    /* تنسيق الأزرار باللون الوردي وتوسيطها */
    .stButton>button {
        background-color: #e75480;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-size: 18px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #c93d6a;
        color: white;
    }
    
    /* تنسيق العبارة الاقتباسية في الواجهة الثانية */
    .butterfly-quote {
        text-align: center;
        font-style: italic;
        color: #ffffff !important;
        background-color: #e75480;
        padding: 15px;
        border-radius: 15px;
        font-size: 18px;
        font-weight: 500;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# إدارة الواجهات والتنقل باستخدام الـ Session State
if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

def reset_pages():
    st.session_state.page = 1

# --- الواجهة الأولى (Page 1): خط Al Dhabi حجم 60، جهة اليسار، الصورة والزر في نفس الشاشة تماماً ---
if st.session_state.page == 1:
    
    # عرض العنوان بالخط والحجم والاتجاه المطلوبين
    st.markdown("<p class='custom-title'>Engineering Titans</p>", unsafe_allow_html=True)
    
    # عرض الصورة لتأخذ كامل عرض الحاوية الافتراضية المتناسقة مع الشاشة مباشرة
    st.image("main_logo.png.jpeg", use_container_width=True)
    
    st.write("")
    if st.button("Next"):
        next_page()

# --- الواجهة الثانية (Page 2): معلومات المريض والشعار الرئيسي ---
elif st.session_state.page == 2:
    st.markdown("<h1 style='font-size: 28px; color: #c93d6a; text-align: center;'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.image("https://i.imgur.com/vHqgZfN.jpeg", width=220)
    
    st.markdown("<p class='butterfly-quote'>\"Like butterflies we flourish when we feel safe\"</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #e75480; font-size: 22px; text-align: center;'>Your health matters ❤️</h3>", unsafe_allow_html=True)
    st.write("---")
    
    st.text_input("Patient Name")
    st.number_input("Patient Age", min_value=1, max_value=120, value=None, placeholder="Enter age")
    st.text_input("Phone Number")
    st.radio("Medical History", ["No", "Yes"], index=0)
    
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_page()
    with col2:
        if st.button("Next"):
            next_page()

# --- الواجهة الثالثة (Page 3): رفع الملف الطبي ---
elif st.session_state.page == 3:
    st.markdown("<h1 style='color: #c93d6a; text-align: center;'>UPLOAD DICOM</h1>", unsafe_allow_html=True)
    st.write("---")
    
    uploaded_file = st.file_uploader("Select DICOM file to analyze ↑", type=["dcm", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully! Ready for AI analysis... ⏳")
        
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_page()
    with col2:
        if st.button("Next"):
            next_page()

# --- الواجهة الرابعة (Page 4): تصنيف الحالة ---
elif st.session_state.page == 4:
    st.markdown("<h1 style='color: #c93d6a; text-align: center;'>Analysis Results - Classification</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h3 style='text-align: left;'>Classification Results:</h3>", unsafe_allow_html=True)
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.success("✨ NORMAL")
    with col_res2:
        st.error("⚠️ ABNORMAL")
        
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #e75480; font-size: 24px; text-align: center;'>Your health matters 🩷</h3>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_page()
    with col2:
        if st.button("Next"):
            next_page()

# --- الواجهة الخامسة والأخيرة (Page 5): خطورة الحالة ---
elif st.session_state.page == 5:
    st.markdown("<h1 style='color: #c93d6a; text-align: center;'>Analysis Results - Severity</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h3 style='text-align: left;'>Severity Assessment:</h3>", unsafe_allow_html=True)
    
    st.info("🟢 BENIGN")
    st.error("🔴 MALIGNANT")
        
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_page()
    with col2:
        if st.button("Reset"):
            reset_pages()
