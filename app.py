
import streamlit as st

# 1. إعدادات الصفحة والأيقونة (تثبيت وضع الصفحة الممتدة Wide لتغطية الشاشة)
st.set_page_config(page_title="Engineering Titans", page_icon="🧬", layout="wide")

# دالة التنسيق الـ CSS لجعل الصورة على كامل واجهة الحاسبة تماماً
st.markdown("""
    <style>
    /* تغيير الخط لكامل الموقع ليكون احترافي ومودرن */
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, p, button, label {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    /* إلغاء الحواف الجانبية للموقع لكي تتمدد الصورة على كامل الشاشة */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* تنسيق الأزرار باللون الوردي (مع وضعها في حاوية متناسقة) */
    .stButton>button {
        background-color: #e75480;
        color: white;
        border-radius: 20px;
        padding: 12px 30px;
        font-size: 18px;
        border: none;
        width: 300px; /* تحديد عرض مناسب للزر وسط الشاشة العريضة */
        font-weight: bold;
        display: block;
        margin: 0 auto !important;
    }
    .stButton>button:hover {
        background-color: #c93d6a;
        color: white;
    }
    
    /* تنسيق العنوان الرئيسي ليكون بارزاً في المنتصف */
    h1 {
        color: #c93d6a;
        text-align: center;
        font-weight: 800;
        font-size: 42px !important;
        margin-bottom: 20px;
    }
    
    /* كود جبار لجعل الصورة تمتد على كبر واجهة الحاسبة بالكامل
