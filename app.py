import streamlit as st

# 1. إعدادات الصفحة لتكون عريضة (Wide) لتغطية واجهة الحاسبة بالكامل
st.set_page_config(page_title="Engineering Titans", page_icon="🧬", layout="wide")

# دالة التنسيق الـ CSS المحدثة لإجبار العنوان على النزول للمكان المطلوب بالسهم
st.markdown("<style> html, body, [data-testid='stMarkdownContainer'], h1, h2, h3, p, button, label { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; } .block-container { padding-top: 8rem !important; /* زيادة المسافة العلوية الافتراضية للموقع بالكامل */ padding-bottom: 1rem !important; padding-left: 0rem !important; padding-right: 0rem !important; max-width: 100% !important; } .stButton>button { background-color: #e75480; color: white; border-radius: 20px; padding: 12px 30px; font-size: 18px; border: none; width: 300px; font-weight: bold; display: block; margin: 0 auto !important; } .stButton>button:hover { background-color: #c93d6a; color: white; } h1 { color: #c93d6a; text-align: center; font-weight: 800; font-size: 46px !important; margin-top: 40px !important; /* دفع العنوان لأسفل إضافي */ margin-bottom: 30px !important; } [data-testid='stImage'] img { width: 100vw !important; max-width: 100vw !important; height: auto !important; object-fit: cover !important; display: block; margin: 0 !important; padding: 0 !important; } [data-testid='stImage'] { width: 100% !important; display: flex !important; justify-content: center !important; } .butterfly-quote { text-align: center; font-style: italic; color: #ffffff !important; background-color: #e75480; padding: 15px; border-radius: 15px; font-size: 18px; font-weight: 500; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); max-width: 600px; margin: 0 auto; } .centered-content { max-width: 700px; margin: 0 auto; padding: 20px; } </style>", unsafe_allow_html=True)

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

# --- الواجهة الأولى (Page 1): العنوان نازل للمكان المطلوب والصورة ملء الشاشة ---
if st.session_state.page == 1:
    # استخدام حاوية مخصصة بمسافة علوية محددة لضمان النزول
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    st.title("Engineering Titans")
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # عرض الصورة لتأخذ كامل عرض واجهة الحاسبة
    st.image("main_logo.png.jpeg", use_container_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.button("Next", on_click=next_page)

# --- الواجهة الثانية (Page 2): معلومات المريض والشعار الرئيسي ---
elif st.session_state.page == 2:
    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 28px;'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
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
        st.button("Back", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

# --- الواجهة الثالثة (Page 3): رفع الملف الطبي ---
elif st.session_state.page == 3:
    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
    st.title("UPLOAD DICOM")
    st.write("---")
    
    uploaded_file = st.file_uploader("Select DICOM file to analyze ↑", type=["dcm", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully! Ready for AI analysis... ⏳")
        
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

# --- الواجهة الرابعة (Page 4): تصنيف الحالة ---
elif st.session_state.page == 4:
    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
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
        st.button("Back", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

# --- الواجهة الخامسة والأخيرة (Page 5): خطورة الحالة ---
elif st.session_state.page == 5:
    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
    st.title("Analysis Results - Severity")
    st.write("---")
    
    st.markdown("<h3 style='text-align: left;'>Severity Assessment:</h3>", unsafe_allow_html=True)
    
    st.info("🟢 BENIGN")
    st.error("🔴 MALIGNANT")
        
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_page)
    with col2:
        st.button("Reset", on_click=reset_pages)
    st.markdown("</div>", unsafe_allow_html=True)
