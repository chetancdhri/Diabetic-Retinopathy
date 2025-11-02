import streamlit as st


def inject_custom_css():
    st.markdown("""
    <style>
        /* Main Styles */
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .main-header {
            font-size: 3.5rem;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 2rem;
            font-weight: 800;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        .section-header {
            font-size: 2.2rem;
            color: #2c3e50;
            margin: 2rem 0 1rem 0;
            padding: 1rem;
            background: linear-gradient(90deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            border-left: 5px solid #667eea;
            font-weight: 700;
        }

        .card {
            background: linear-gradient(135deg, #6bcf7f, #4ca2cd);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        }

        .metric-card {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .risk-high { 
            background: linear-gradient(135deg, #ff6b6b, #ee5a52);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-weight: bold;
        }

        .risk-medium { 
            background: linear-gradient(135deg, #ffd93d, #ff9a3d);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-weight: bold;
        }

        .risk-low { 
            background: linear-gradient(135deg, #6bcf7f, #4ca2cd);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-weight: bold;
        }

        /* Sidebar Styles */
        .css-1d391kg {
            background: linear-gradient(180deg, #2c3e50, #3498db);
        }

        /* Button Styles */
        .stButton>button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        /* Chat Styles */
        .chat-message {
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .user-message {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            margin-left: 20%;
        }

        .assistant-message {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border: 1px solid rgba(0,0,0,0.1);
            margin-right: 20%;
        }

        /* Progress Bar */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        /* File Uploader */
        .uploadedFile {
            background: rgba(255, 255, 255, 0.9);
            border: 2px dashed #667eea;
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
        }

        /* Tab Styles */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background: rgba(255,255,255,0.8);
            border-radius: 10px 10px 0px 0px;
            gap: 1rem;
            padding: 1rem 2rem;
            font-weight: 600;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)


def create_feature_card(title, description, icon="🔬"):
    return f"""
    <div class="card">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
            <h3 style="margin: 0; color: #2c3e50;">{title}</h3>
        </div>
        <p style="color: #7f8c8d; line-height: 1.6;">{description}</p>
    </div>
    """