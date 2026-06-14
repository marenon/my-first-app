import streamlit as st

# 1. إعدادات الصفحة والأيقونة (تعديل الأيقونة لتكون رسمية بدون فيونكة)
st.set_page_config(page_title="Engineering Titans", page_icon="🧬", layout="centered")

# دالة التنسيق الـ CSS لتغيير الخطوط، الألوان، وتوسيط العناصر
st.markdown("""
    <style>
    /* تغيير الخط لكامل الموقع ليكون احترافي ومودرن */
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, p, button, label {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    /* تنسيق الأزرار باللون الوردي */
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
    
    /* تنسيق العناوين الرئيسية باللون الوردي وضمان توسيطها */
    h1, h2, h3 {
        color: #c93d6a;
        text-align: center;
        font-weight: 700;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* تنسيق العبارة الاقتباسية لتكون باللون الأبيض مع خلفية وردية ناعمة لتبرز */
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
    
    /* كود قوي لإجبار الصور على التوسط في منتصف الشاشة تماماً */
    [data-testid="stImage"] img {
        display: block;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center !important;
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

# --- الواجهة الأولى (Page 1): الاسم فوق والصورة مكبرة في الوسط ---
if st.session_state.page == 1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 1. العنوان المحدث بدون الفيونكة
    st.title("Engineering Titans")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. عرض الصورة بحجم أكبر (width=600) وتوسيطها بالمنتصف
    st.image("main_logo.png.jpeg", width=600)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Next"):
        next_page()

# --- الواجهة الثانية (Page 2): معلومات المريض والشعار الرئيسي ---
elif st.session_state.page == 2:
    st.markdown("<h1 style='font-size: 28px;'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # عرض صورة الفراشة والشريط
    st.image("https://i.imgur.com/vHqgZfN.jpeg", width=220)
    
    # العبارة الاقتباسية باللون الأبيض داخل بطاقة وردية أنيقة
    st.markdown("<p class='butterfly-quote'>\"Like butterflies we flourish when we feel safe\"</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #e75480; font-size: 22px;'>Your health matters ❤️</h3>", unsafe_allow_html=True)
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
    st.title("UPLOAD DICOM")
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
    st.title("Analysis Results - Classification")
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
    st.title("Analysis Results - Severity")
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
