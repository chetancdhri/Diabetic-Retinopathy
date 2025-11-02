import streamlit as st
import random
from datetime import datetime


class DRChatbot:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Hello! I'm your Diabetic Retinopathy AI Assistant. How can I help you today? 👁️",
                "Hi there! I'm here to assist with diabetic retinopathy questions. What would you like to know? 🩺",
                "Welcome! I'm your AI consultant for diabetic retinopathy screening and information. How can I assist? 🔍"
            ],
            "symptoms": [
                "Common symptoms include blurred vision, floaters, dark areas in vision, difficulty perceiving colors, and vision loss.",
                "Watch for: blurred vision, spots or dark strings floating, vision fluctuations, impaired color vision, and dark spots.",
                "Symptoms progress from mild (microaneurysms) to severe (neovascularization). Early stages often show no symptoms."
            ],
            "stages": [
                "Diabetic retinopathy has 4 stages: 1) Mild NPDR, 2) Moderate NPDR, 3) Severe NPDR, 4) Proliferative DR.",
                "Stages progress from mild non-proliferative to proliferative DR. Early detection at mild stage is crucial.",
                "The stages are: No DR → Mild → Moderate → Severe NPDR → Proliferative DR with increasing vision risk."
            ],
            "prevention": [
                "Control blood sugar, maintain healthy BP/cholesterol, regular eye exams, quit smoking, and exercise regularly.",
                "Key prevention: Annual eye exams, HbA1c <7%, BP <130/80, healthy diet, and no smoking.",
                "Prevent progression with: Regular screening, glucose control, blood pressure management, and lifestyle changes."
            ],
            "treatment": [
                "Treatments include laser surgery, anti-VEGF injections, vitrectomy, and corticosteroids based on severity.",
                "Options: Laser photocoagulation, intravitreal injections, vitrectomy surgery, and proper diabetes management.",
                "Treatment depends on stage: Mild - monitoring; Moderate - laser; Severe - injections/surgery."
            ],
            "screening": [
                "Diabetics should have annual eye exams. More frequent if DR detected. Use AI screening for early detection.",
                "Screen annually for Type 2 diabetes, 5 years after diagnosis for Type 1, and more often if retinopathy present.",
                "Regular screening includes: Visual acuity test, dilated eye exam, tonometry, and retinal imaging."
            ],
            "risk_factors": [
                "Risk factors: Diabetes duration, poor glucose control, high blood pressure, high cholesterol, pregnancy, smoking.",
                "Higher risk with: Long diabetes history, high HbA1c, hypertension, nephropathy, and tobacco use.",
                "Key risks: Duration of diabetes, blood sugar levels, blood pressure, cholesterol, and genetic factors."
            ],
            "default": [
                "I specialize in diabetic retinopathy. Could you ask about symptoms, stages, prevention, treatment, or screening?",
                "I'm here to help with diabetic retinopathy questions. Try asking about stages, symptoms, or prevention methods.",
                "As a DR specialist, I can discuss screening, symptoms, treatments, or risk factors. What interests you?"
            ]
        }

        self.context_keywords = {
            "hello": "greeting", "hi": "greeting", "hey": "greeting",
            "symptom": "symptoms", "vision": "symptoms", "blur": "symptoms",
            "stage": "stages", "level": "stages", "grade": "stages",
            "prevent": "prevention", "avoid": "prevention", "stop": "prevention",
            "treat": "treatment", "cure": "treatment", "therapy": "treatment",
            "screen": "screening", "test": "screening", "exam": "screening",
            "risk": "risk_factors", "factor": "risk_factors", "cause": "risk_factors"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Check for context keywords
        for keyword, context in self.context_keywords.items():
            if keyword in user_input:
                return random.choice(self.responses[context])

        # Default response
        return random.choice(self.responses["default"])

    def get_suggested_questions(self):
        return [
            "What are the early symptoms of diabetic retinopathy?",
            "How often should I get screened for DR?",
            "What are the different stages of diabetic retinopathy?",
            "How can I prevent diabetic retinopathy?",
            "What treatments are available for severe DR?",
            "What are the main risk factors for developing DR?"
        ]


def initialize_chat_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = DRChatbot()

        # Add welcome message
        welcome_msg = random.choice(st.session_state.chatbot.responses["greeting"])
        st.session_state.chat_history.append({
            "role": "assistant",
            "message": welcome_msg,
            "timestamp": datetime.now()
        })


def display_chat_interface():
    st.markdown("### 💬 AI Chat Assistant")

    # Chat container
    chat_container = st.container()

    # Display chat history
    with chat_container:
        for chat in st.session_state.chat_history:
            if chat["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You:</strong> {chat["message"]}
                    <div style="font-size: 0.8rem; opacity: 0.7; text-align: right;">
                        {chat["timestamp"].strftime("%H:%M")}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message assistant-message">
                    <strong>👁️ DR Assistant:</strong> {chat["message"]}
                    <div style="font-size: 0.8rem; opacity: 0.7; text-align: right;">
                        {chat["timestamp"].strftime("%H:%M")}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Suggested questions
    st.markdown("### 💡 Suggested Questions")
    suggested_questions = st.session_state.chatbot.get_suggested_questions()

    cols = st.columns(2)
    for i, question in enumerate(suggested_questions):
        with cols[i % 2]:
            if st.button(question, key=f"suggest_{i}"):
                # Add user question to chat
                st.session_state.chat_history.append({
                    "role": "user",
                    "message": question,
                    "timestamp": datetime.now()
                })

                # Get and add bot response
                response = st.session_state.chatbot.get_response(question)
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "message": response,
                    "timestamp": datetime.now()
                })

                st.rerun()

    # User input
    st.markdown("---")
    user_input = st.text_input("💭 Ask me anything about diabetic retinopathy:",
                               placeholder="Type your question here...")

    if user_input:
        # Add user message to chat
        st.session_state.chat_history.append({
            "role": "user",
            "message": user_input,
            "timestamp": datetime.now()
        })

        # Get bot response
        response = st.session_state.chatbot.get_response(user_input)
        st.session_state.chat_history.append({
            "role": "assistant",
            "message": response,
            "timestamp": datetime.now()
        })

        st.rerun()