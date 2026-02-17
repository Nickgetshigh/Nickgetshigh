import streamlit as st
import time
import streamlit_confetti as confetti  # Optional: pip install streamlit-confetti

# Page config for production: wide layout, mobile-friendly, favicon
st.set_page_config(
    page_title="🙏 Farewell Guru Ankit Sharma 🙏",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for festive, professional theme - inspired by production best practices
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    .guru-card {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
    }
    .junior-card {
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    h1 { color: #fff; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    </style>
""", unsafe_allow_html=True)

# Session state for interactions - production-ready state management
if 'farewell_clicked' not in st.session_state:
    st.session_state.farewell_clicked = False
if 'guru_sent' not in st.session_state:
    st.session_state.guru_sent = False
if 'juniors_sent' not in st.session_state:
    st.session_state.juniors_sent = False

# Header
st.title("🌟 Guru Ankit Sharma को विदाई 🌟")
st.markdown("**Real Guru & Nanhe Munne Juniors के लिए Special Farewell App**")

# Main content in columns for responsive design
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="guru-card">', unsafe_allow_html=True)
    st.markdown("### 🙏 Guru Ankit Sharma 🙏")
    st.markdown("""
    Dear Ankit Bhaiya / Guru ji,  
    आपने हमें न सिर्फ कोडिंग सिखाई, बल्कि जीवन के गुर भी दिए।  
    हर debug session, हर late-night call - वो सब यादें हमेशा रहेंगी।  
    Thank you for being our Big Brother, Mentor & Guide!  
    All the best for new adventures! 🚀
    """)
    
    if st.button("🎁 Send Farewell to Guru", key="guru_btn"):
        st.session_state.guru_sent = True
        st.session_state.farewell_clicked = True
        st.balloons()
        if 'confetti' in locals():
            confetti.show()  # Extra confetti if installed
        st.success("Farewell sent to Guru Ankit! 🎊")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="junior-card">', unsafe_allow_html=True)
    st.markdown("### 🍼 Nanhe Munne Juniors 🍼")
    st.markdown("""
    Dear Juniors,  
    Guru Ankit के जाने से team अधूरी लगेगी, लेकिन lessons हमेशा साथ रहेंगे।  
    Keep learning, keep coding, और कभी हार मत मानना!  
    We wish you all the best! 💪✨
    """)
    
    if st.button("📝 Send Message to Juniors", key="juniors_btn"):
        st.session_state.juniors_sent = True
        st.session_state.farewell_clicked = True
        st.balloons()
        if 'confetti' in locals():
            confetti.show()
        st.success("Message sent to Juniors! 🎈")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer with share & rerun
if st.session_state.farewell_clicked:
    st.markdown("---")
    st.success("🌈 Farewell Celebration Complete! Share this app with the team. 👇")
    st.info("Deploy on Streamlit Cloud for free: Connect GitHub repo & deploy instantly.[web:19]")

# Sidebar for extras - production polish
with st.sidebar:
    st.markdown("### 🎉 App Controls")
    if st.button("🔄 Reset Celebration"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    st.markdown("**Production Tips:**")
    st.markdown("- Mobile responsive")
    st.markdown("- Custom theme & animations")
    st.markdown("- Deploy: `streamlit run farewell_ankit.py`")
    st.markdown("- Cloud: Streamlit Community Cloud / Azure[web:19]")

# Auto-celebration after actions
if st.session_state.guru_sent and st.session_state.juniors_sent:
    time.sleep(1)
    st.balloons()
    st.markdown("**Team Farewell Complete! Thank you Ankit Sharma! 🇮🇳**"[web:18])
