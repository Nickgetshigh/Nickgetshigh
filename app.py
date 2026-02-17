import streamlit as st
import time

# Production config
st.set_page_config(
    page_title="🙏 Guru Ankit Sharma Farewell 🙏",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Festive CSS theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    .guru-card {
        background: rgba(255,255,255,0.95);
        border-radius: 25px;
        padding: 2.5rem;
        box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        text-align: center;
        margin: 1rem 0;
        border: 3px solid #FFD700;
    }
    .junior-card {
        background: rgba(255,255,255,0.92);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        text-align: center;
        margin: 1rem 0;
        border: 2px solid #4ECDC4;
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
        color: white !important;
        border: none;
        border-radius: 50px;
        padding: 1.2rem 2.5rem;
        font-weight: 700;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    h1 { 
        color: #fff; 
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        font-size: 3rem;
    }
    .big-text {
        font-size: 1.4rem;
        color: #2c3e50;
        font-weight: 600;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Session state
if 'guru_clicked' not in st.session_state:
    st.session_state.guru_clicked = False
if 'juniors_clicked' not in st.session_state:
    st.session_state.juniors_clicked = False
if 'celebration_done' not in st.session_state:
    st.session_state.celebration_done = False

# Header
st.title("🌟 Guru Ankit Sharma को Heartfelt विदाई 🌟")
st.markdown("**Real Guru & हमारे Nanhe Munne Juniors के लिए Special App**")

# ✅ FIXED: Use valid gap="large"
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="guru-card">', unsafe_allow_html=True)
    st.markdown("### 🙏 *Guru Ankit Sharma ji* 🙏")
    st.markdown("""
    <div class="big-text">
    🎯 **Ankit Bhaiya**, आपने हमें सिर्फ कोडिंग नहीं, **जीवन का गुर** सिखाया।<br>
    🕒 हर late-night debug session, हर problem-solving call - **हमेशा याद रहेंगे**।<br>
    💡 आपकी guidance ने हमें **real professionals** बनाया।<br>
    🚀 New adventures के लिए **All the very best Guru ji**!<br><br>
    **Team forever grateful 🙏**
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎁 Guru को Farewell भेजें", key="guru_btn"):
        st.session_state.guru_clicked = True
        st.balloons()
        st.balloons()
        st.success("✨ Guru Ankit को Farewell successfully भेजा गया! 🎊")
        st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="junior-card">', unsafe_allow_html=True)
    st.markdown("### 🍼 *हमारे Nanhe Munne Juniors* 🍼")
    st.markdown("""
    <div class="big-text">
    📚 Guru Ankit के **lessons हमेशा साथ रहेंगे**।<br>
    💪 Keep learning, keep coding, **कभी हार मत मानना**!<br>
    🌟 आप सबके bright future के लिए **best wishes**!<br>
    🎯 Guru ji की teachings follow करते रहना।<br><br>
    **Team's love & support 💙**
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("💌 Juniors को Message भेजें", key="juniors_btn"):
        st.session_state.juniors_clicked = True
        st.snow()
        st.success("🎈 Juniors को message successfully भेजा गया! ❄️")
        st.snow()

    st.markdown('</div>', unsafe_allow_html=True)

# Celebration section
if st.session_state.guru_clicked or st.session_state.juniors_clicked:
    st.markdown("---")
    st.markdown('<div style="text-align: center; padding: 2rem; background: linear-gradient(45deg, #FF6B6B, #4ECDC4); border-radius: 20px; color: white; font-size: 1.5rem; font-weight: 700;">', unsafe_allow_html=True)
    st.markdown("🎉 **Complete Team Farewell Celebration!** 🎉")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.session_state.guru_clicked and st.session_state.juniors_clicked and not st.session_state.celebration_done:
        st.session_state.celebration_done = True
        for i in range(3):
            st.balloons()
            st.snow()
            time.sleep(0.5)
        st.markdown("**🇮🇳 Guru Ankit Sharma - आप हमेशा हमारे दिल में! 🙏**")

# Footer
st.markdown("---")
col_left, col_right = st.columns([2, 1])  # ✅ No gap param needed for simple columns

with col_left:
    st.success("✅ **Production Ready** - Deployed on Streamlit Cloud")
    st.info("👨‍💻 Made with ❤️ for Team & Guru Ankit Sharma")

with col_right:
    st.markdown("**Share:**")
    st.code("https://nickgetshigh-axyzcg4s8ysyj3gouov7jh.streamlit.app")

# Sidebar
with st.sidebar:
    st.markdown("### 🎮 **App Controls**")
    if st.button("🔄 Reset Celebration", use_container_width=True):
        st.session_state.guru_clicked = False
        st.session_state.juniors_clicked = False
        st.session_state.celebration_done = False
        st.rerun()
    
    st.markdown("---")
    st.markdown("**🚀 Production Features:**")
    st.markdown("- ✅ Zero external dependencies")
    st.markdown("- ✅ Mobile responsive")
    st.markdown("- ✅ Native animations")
    st.markdown("- ✅ Session state")

st.markdown("---")
st.caption("💙 *Team's tribute to our Real Guru Ankit Sharma ji*")
