import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
import base64
from utils.helpers import EnhancedDRHelper, generate_sample_patients
from utils.chatbot import initialize_chat_session, display_chat_interface
from utils.styles import inject_custom_css, create_feature_card
from components.charts import create_patient_demographics_chart, create_treatment_effectiveness_chart, \
    create_progression_timeline

# Page configuration
st.set_page_config(
    page_title="DR AI Consultancy Pro",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
inject_custom_css()

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

if 'current_view' not in st.session_state:
    st.session_state.current_view = "dashboard"


# Initialize helper classes
@st.cache_resource
def get_dr_helper():
    return EnhancedDRHelper()


dr_helper = get_dr_helper()


def main():
    # Header with navigation
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<h1 class="main-header">👁️ Diabetic Retinopathy AI Consultancy Pro</h1>', unsafe_allow_html=True)

    # Main navigation
    st.sidebar.markdown("## 🧭 Navigation")

    app_mode = st.sidebar.radio(
        "Choose Section",
        ["🏠 Dashboard", "🔍 DR Analysis", "👥 Patient Management", "💬 AI Assistant", "📚 Knowledge Base", "📊 Analytics"]
    )

    # Quick stats in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📈 Quick Stats")

    sample_patients = generate_sample_patients(100)
    total_patients = len(sample_patients)
    high_risk = len(sample_patients[sample_patients['dr_stage'] >= 3])
    avg_hba1c = sample_patients['hba1c'].mean()

    st.sidebar.metric("Total Patients", f"{total_patients:,}")
    st.sidebar.metric("High Risk Cases", f"{high_risk}")
    st.sidebar.metric("Avg HbA1c", f"{avg_hba1c:.1f}%")

    # Route to appropriate section
    if "Dashboard" in app_mode:
        show_dashboard()
    elif "DR Analysis" in app_mode:
        show_dr_analysis()
    elif "Patient Management" in app_mode:
        show_patient_management()
    elif "AI Assistant" in app_mode:
        show_ai_assistant()
    elif "Knowledge Base" in app_mode:
        show_knowledge_base()
    elif "Analytics" in app_mode:
        show_analytics()


def show_dashboard():
    st.markdown('<h2 class="section-header">🏠 AI-Powered DR Screening Dashboard</h2>', unsafe_allow_html=True)

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🩺 Patients Screened</h3>
            <h2>1,247</h2>
            <p>+12% this month</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🔍 Early Detection</h3>
            <h2>89%</h2>
            <p>+5% improvement</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>⚡ Avg Processing</h3>
            <h2>2.3s</h2>
            <p>-0.5s faster</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Accuracy</h3>
            <h2>94%</h2>
            <p>+2% from baseline</p>
        </div>
        """, unsafe_allow_html=True)

    # Features overview
    st.markdown("## 🚀 Platform Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(create_feature_card(
            "AI-Powered Analysis",
            "Advanced machine learning algorithms for precise diabetic retinopathy detection and classification with 94% accuracy.",
            "🤖"
        ), unsafe_allow_html=True)

        st.markdown(create_feature_card(
            "Real-time Screening",
            "Instant analysis of retinal images with comprehensive feature detection and severity assessment in under 3 seconds.",
            "⚡"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(create_feature_card(
            "Patient Management",
            "Complete patient tracking, progress monitoring, and automated follow-up scheduling with risk assessment.",
            "👥"
        ), unsafe_allow_html=True)

        st.markdown(create_feature_card(
            "AI Chat Assistant",
            "24/7 intelligent assistant for DR-related queries, treatment guidance, and educational support.",
            "💬"
        ), unsafe_allow_html=True)

    # Recent activity and charts
    st.markdown("## 📊 Recent Activity Overview")

    sample_data = generate_sample_patients(50)
    fig1, fig2, fig3, fig4 = create_patient_demographics_chart(sample_data)

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)


def show_dr_analysis():
    st.markdown('<h2 class="section-header">🔍 Advanced DR Analysis</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 📤 Image Upload")

        uploaded_file = st.file_uploader(
            "Upload Retinal Fundus Image",
            type=['png', 'jpg', 'jpeg', 'tiff'],
            help="Supported formats: PNG, JPG, JPEG, TIFF"
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Retinal Image", use_column_width=True)

            # Analysis options
            st.markdown("### ⚙️ Analysis Options")

            col_a, col_b = st.columns(2)
            with col_a:
                detailed_analysis = st.checkbox("Detailed Feature Analysis", value=True)
                severity_scoring = st.checkbox("Severity Scoring", value=True)
            with col_b:
                risk_assessment = st.checkbox("Risk Assessment", value=True)
                treatment_recommendations = st.checkbox("Treatment Recommendations", value=True)

            if st.button("🚀 Start Comprehensive Analysis", type="primary", use_container_width=True):
                with st.spinner("🔬 Analyzing retinal image with AI..."):
                    # Simulate processing time
                    import time
                    progress_bar = st.progress(0)

                    for i in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(i + 1)

                    # Perform analysis
                    analysis_results = dr_helper.generate_comprehensive_analysis(image)
                    st.session_state.analysis_results = analysis_results

                    st.success("✅ Analysis completed successfully!")

        else:
            # Demo option
            st.markdown("### 🎯 Quick Demo")
            if st.button("Use Sample Image for Demonstration", use_container_width=True):
                # Create sample image
                sample_image = Image.new('RGB', (512, 512), color='darkred')
                analysis_results = dr_helper.generate_comprehensive_analysis(sample_image)
                st.session_state.analysis_results = analysis_results
                st.rerun()

    with col2:
        if st.session_state.analysis_results:
            display_comprehensive_results(st.session_state.analysis_results)
        else:
            show_analysis_guidelines()


def display_comprehensive_results(results):
    """Display comprehensive analysis results"""
    st.markdown("## 📋 Comprehensive Analysis Report")

    # Severity Overview
    col1, col2 = st.columns([1, 2])

    with col1:
        st.plotly_chart(dr_helper.create_enhanced_severity_gauge(results['severity_score']),
                        use_container_width=True)

        # Key metrics
        st.markdown("### 📊 Key Metrics")
        col_a, col_b = st.columns(2)

        with col_a:
            st.metric("Confidence Score", f"{results['confidence']:.1%}")
            st.metric("Processing Time", f"{results['processing_time']:.2f}s")

        with col_b:
            st.metric("Image Quality", results['image_quality']['grade'])
            st.metric("Progression Risk", f"{results['progression_risk']:.1%}")

    with col2:
        stage_info = results['stage_info']
        st.markdown(f"### 🎯 Current Stage: **{stage_info['name']}**")
        st.markdown(f"**Description:** {stage_info['description']}")
        st.markdown(
            f"**Risk Level:** <span class='risk-{stage_info['risk'].lower().split()[0]}'>{stage_info['risk']}</span>",
            unsafe_allow_html=True)
        st.markdown(f"**Recommended Follow-up:** {stage_info['follow_up']}")

    # Detailed Features
    st.markdown("## 🔍 Detailed Feature Analysis")

    features = results['features']
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Microaneurysms", features['microaneurysms']['count'])
    with col2:
        st.metric("Hemorrhages", features['hemorrhages']['count'])
    with col3:
        st.metric("Exudates", features['exudates']['count'])
    with col4:
        st.metric("Cotton Wool Spots", features['cotton_wool_spots']['count'])

    # Risk Assessment
    st.markdown("## ⚠️ Comprehensive Risk Assessment")

    for risk in results['risk_assessment']:
        risk_class = f"risk-{risk['level'].replace(' ', '-').lower()}"
        st.markdown(f"- <span class='{risk_class}'>{risk['type']}</span>",
                    unsafe_allow_html=True)

    # Recommendations
    st.markdown("## 💡 Treatment & Management Recommendations")

    for i, recommendation in enumerate(results['recommendations'], 1):
        st.markdown(f"{i}. **{recommendation}**")

    # Action Buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📥 Download Full Report", use_container_width=True):
            st.success("Report download feature would be implemented here!")

    with col2:
        if st.button("📅 Schedule Follow-up", use_container_width=True):
            st.info("Follow-up scheduling modal would open here!")

    with col3:
        if st.button("🔄 Analyze New Image", use_container_width=True):
            st.session_state.analysis_results = None
            st.rerun()


def show_analysis_guidelines():
    """Show analysis guidelines when no image is uploaded"""
    st.markdown("""
    <div class="card">
        <h2>🎯 How to Use DR Analysis</h2>
        <p>Upload a retinal fundus image to get started with AI-powered analysis:</p>

        <h3>📋 Preparation Guidelines:</h3>
        <ul>
            <li>Use high-quality retinal fundus images</li>
            <li>Ensure proper illumination and focus</li>
            <li>Image format: PNG, JPG, JPEG, or TIFF</li>
            <li>Minimum resolution: 512x512 pixels</li>
            <li>Include macula and optic disc when possible</li>
        </ul>

        <h3>🔍 What We Analyze:</h3>
        <ul>
            <li><strong>Microaneurysms:</strong> Early indicators of DR</li>
            <li><strong>Hemorrhages:</strong> Blood vessel leakage markers</li>
            <li><strong>Exudates:</strong> Lipid deposits indicating edema</li>
            <li><strong>Cotton Wool Spots:</strong> Nerve fiber layer infarcts</li>
            <li><strong>Severity Scoring:</strong> International DR scale (0-4)</li>
        </ul>

        <h3>⚡ Expected Output:</h3>
        <ul>
            <li>Comprehensive severity assessment</li>
            <li>Detailed feature analysis</li>
            <li>Personalized recommendations</li>
            <li>Risk progression analysis</li>
            <li>Downloadable medical report</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def show_patient_management():
    st.markdown('<h2 class="section-header">👥 Advanced Patient Management</h2>', unsafe_allow_html=True)

    # Generate sample patient data
    patients_df = generate_sample_patients(100)

    # Filters
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age_range = st.slider("Age Range", 20, 80, (30, 70))
    with col2:
        dr_stages = st.multiselect("DR Stages", [0, 1, 2, 3, 4], default=[0, 1, 2, 3, 4])
    with col3:
        hba1c_range = st.slider("HbA1c Range", 5.0, 12.0, (6.0, 9.0))
    with col4:
        risk_level = st.selectbox("Risk Level", ["All", "Low", "Moderate", "High", "Very High"])

    # Filter data
    filtered_df = patients_df[
        (patients_df['age'] >= age_range[0]) &
        (patients_df['age'] <= age_range[1]) &
        (patients_df['dr_stage'].isin(dr_stages)) &
        (patients_df['hba1c'] >= hba1c_range[0]) &
        (patients_df['hba1c'] <= hba1c_range[1])
        ]

    if risk_level != "All":
        risk_mapping = {"Low": [0, 1], "Moderate": [2], "High": [3], "Very High": [4]}
        filtered_df = filtered_df[filtered_df['dr_stage'].isin(risk_mapping[risk_level])]

    # Display patient data
    st.markdown(f"### 📋 Patient Records ({len(filtered_df)} found)")
    st.dataframe(filtered_df, use_container_width=True, height=400)

    # Patient details
    if not filtered_df.empty:
        st.markdown("### 👤 Selected Patient Details")
        selected_patient = st.selectbox("Select Patient", filtered_df['patient_id'].tolist())

        if selected_patient:
            patient_data = filtered_df[filtered_df['patient_id'] == selected_patient].iloc[0]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("**Personal Information**")
                st.write(f"Name: {patient_data['name']}")
                st.write(f"Age: {patient_data['age']}")
                st.write(f"Gender: {patient_data['gender']}")

            with col2:
                st.markdown("**Medical Information**")
                st.write(f"Diabetes Type: {patient_data['diabetes_type']}")
                st.write(f"Duration: {patient_data['diabetes_duration']} years")
                st.write(f"HbA1c: {patient_data['hba1c']}%")

            with col3:
                st.markdown("**DR Status**")
                stage_info = dr_helper.stages[patient_data['dr_stage']]
                st.write(f"DR Stage: {stage_info['name']}")
                st.write(f"Risk Score: {patient_data['risk_score']}%")
                st.write(f"Last Screening: {patient_data['last_screening']}")


def show_ai_assistant():
    st.markdown('<h2 class="section-header">💬 AI Chat Assistant</h2>', unsafe_allow_html=True)

    # Initialize chat session
    initialize_chat_session()

    # Display chat interface
    display_chat_interface()


def show_knowledge_base():
    st.markdown('<h2 class="section-header">📚 Diabetic Retinopathy Knowledge Base</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🎯 DR Stages", "🔍 Symptoms", "💊 Treatments", "🛡️ Prevention", "📖 Guidelines"])

    with tab1:
        st.markdown("## Diabetic Retinopathy Stages")

        for stage_num, stage_info in dr_helper.stages.items():
            with st.expander(f"Stage {stage_num}: {stage_info['name']}", expanded=stage_num == 0):
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"**Description:** {stage_info['description']}")
                    st.markdown(f"**Risk Level:** {stage_info['risk']}")
                    st.markdown(f"**Follow-up:** {stage_info['follow_up']}")

                with col2:
                    st.markdown(
                        f"<div style='background-color: {stage_info['color']}; padding: 1rem; border-radius: 10px; color: white; text-align: center;'>"
                        f"<h3>Stage {stage_num}</h3></div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("## Symptoms and Clinical Findings")

        symptoms_data = {
            "Early Stage": ["Often asymptomatic", "Mild vision fluctuations", "Microaneurysms visible on imaging"],
            "Moderate Stage": ["Blurred vision", "Difficulty reading", "Retinal hemorrhages", "Cotton wool spots"],
            "Advanced Stage": ["Significant vision loss", "Floaters", "Dark spots", "Impaired color vision",
                               "Macular edema"],
            "Proliferative Stage": ["Severe vision loss", "Vitreous hemorrhage", "Retinal detachment",
                                    "Neovascularization"]
        }

        for stage, symptoms in symptoms_data.items():
            st.markdown(f"### {stage}")
            for symptom in symptoms:
                st.markdown(f"- {symptom}")

    with tab3:
        st.markdown("## Treatment Options by Stage")

        st.plotly_chart(create_treatment_effectiveness_chart(), use_container_width=True)

        for severity, treatments in dr_helper.treatment_options.items():
            st.markdown(f"### {severity} DR")
            for treatment in treatments:
                st.markdown(f"- **{treatment}**")

    with tab4:
        st.markdown("## Prevention Strategies")

        prevention_methods = {
            "🎯 Blood Sugar Control": "Maintain HbA1c below 7% through medication, diet, and exercise",
            "🩺 Regular Screening": "Annual eye exams for all diabetic patients, more frequent if DR detected",
            "💊 Blood Pressure Management": "Keep BP below 130/80 mmHg with medication and lifestyle changes",
            "🥗 Healthy Lifestyle": "Balanced diet, regular exercise, weight management, smoking cessation",
            "📊 Cholesterol Control": "Manage lipid levels through diet and medication if needed",
            "👁️ Early Detection": "Use AI screening tools for regular monitoring and early intervention"
        }

        cols = st.columns(2)
        for i, (method, description) in enumerate(prevention_methods.items()):
            with cols[i % 2]:
                st.markdown(f"**{method}**")
                st.markdown(f"<div style='color: #7f8c8d;'>{description}</div>", unsafe_allow_html=True)
                st.markdown("---")

    with tab5:
        st.markdown("## Clinical Guidelines")

        guidelines = {
            "Screening Frequency": {
                "Type 1 Diabetes": "Annual screening starting 5 years after diagnosis",
                "Type 2 Diabetes": "Annual screening from time of diagnosis",
                "Pregnancy": "First trimester and close monitoring throughout pregnancy",
                "Established DR": "3-12 months based on severity"
            },
            "Referral Criteria": {
                "Urgent Referral": "PDR, vitreous hemorrhage, retinal detachment",
                "Early Referral": "Severe NPDR, clinically significant macular edema",
                "Routine Referral": "Moderate NPDR with poor risk factor control"
            },
            "Monitoring Parameters": {
                "Metabolic": "HbA1c every 3-6 months, target <7%",
                "Ocular": "Visual acuity, retinal imaging, OCT when indicated",
                "Systemic": "Blood pressure, lipid profile, renal function"
            }
        }

        for category, items in guidelines.items():
            st.markdown(f"### {category}")
            for item, description in items.items():
                st.markdown(f"- **{item}:** {description}")


def show_analytics():
    st.markdown('<h2 class="section-header">📊 Advanced Analytics</h2>', unsafe_allow_html=True)

    # Generate comprehensive analytics
    patients_df = generate_sample_patients(200)

    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        avg_hba1c = patients_df['hba1c'].mean()
        st.metric("Average HbA1c", f"{avg_hba1c:.1f}%")

    with col2:
        progression_cases = len(patients_df[patients_df['dr_stage'] >= 2])
        st.metric("Progression Cases", f"{progression_cases}")

    with col3:
        avg_duration = patients_df['diabetes_duration'].mean()
        st.metric("Avg Diabetes Duration", f"{avg_duration:.1f} years")

    with col4:
        high_risk_patients = len(patients_df[patients_df['risk_score'] > 70])
        st.metric("High Risk Patients", f"{high_risk_patients}")

    # Advanced charts
    col1, col2 = st.columns(2)

    with col1:
        # Treatment effectiveness
        st.plotly_chart(create_treatment_effectiveness_chart(), use_container_width=True)

        # Risk factor correlation
        corr_data = patients_df[['age', 'diabetes_duration', 'hba1c', 'bp_systolic', 'risk_score']].corr()
        fig_corr = px.imshow(corr_data, title='Risk Factors Correlation Matrix',
                             color_continuous_scale='RdBu_r', aspect="auto")
        st.plotly_chart(fig_corr, use_container_width=True)

    with col2:
        # Progression timeline
        st.plotly_chart(create_progression_timeline(), use_container_width=True)

        # Age distribution by DR stage
        fig_age_stage = px.box(patients_df, x='dr_stage', y='age',
                               title='Age Distribution by DR Stage',
                               color='dr_stage')
        st.plotly_chart(fig_age_stage, use_container_width=True)

    # Predictive analytics section
    st.markdown("## 🔮 Predictive Analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Progression Risk Prediction")

        # Mock prediction inputs
        age = st.slider("Patient Age", 25, 80, 55)
        duration = st.slider("Diabetes Duration (years)", 1, 30, 10)
        hba1c = st.slider("Current HbA1c", 5.0, 12.0, 7.5)
        current_stage = st.selectbox("Current DR Stage", [0, 1, 2, 3])

        if st.button("Predict Progression Risk"):
            # Mock prediction calculation
            base_risk = current_stage * 0.2
            duration_risk = min(duration / 30, 1) * 0.3
            hba1c_risk = min((hba1c - 5.5) / 6.5, 1) * 0.3
            age_risk = min(age / 80, 1) * 0.2

            progression_risk = (base_risk + duration_risk + hba1c_risk + age_risk) * 100

            st.metric("1-Year Progression Risk", f"{progression_risk:.1f}%")

    with col2:
        st.markdown("### Treatment Outcome Prediction")

        treatment_type = st.selectbox("Treatment Type",
                                      ["Laser Therapy", "Anti-VEGF", "Combination", "Observation"])
        patient_risk = st.slider("Patient Risk Score", 0, 100, 65)

        if st.button("Predict Treatment Outcome"):
            # Mock outcome prediction
            base_success = {"Laser Therapy": 65, "Anti-VEGF": 78, "Combination": 85, "Observation": 30}
            success_rate = base_success[treatment_type] * (1 - patient_risk / 200)

            st.metric("Predicted Success Rate", f"{success_rate:.1f}%")


if __name__ == "__main__":
    main()