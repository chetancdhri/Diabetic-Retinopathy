import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image, ImageDraw, ImageFont
import cv2
import random
from faker import Faker
import io
import base64

fake = Faker()


class EnhancedDRHelper:
    def __init__(self):
        self.stages = {
            0: {
                "name": "No Diabetic Retinopathy",
                "description": "No visible retinal abnormalities",
                "risk": "Low",
                "follow_up": "Annual screening",
                "color": "#2ecc71"
            },
            1: {
                "name": "Mild Non-Proliferative DR",
                "description": "Microaneurysms only",
                "risk": "Low to Moderate",
                "follow_up": "6-12 month follow-up",
                "color": "#f39c12"
            },
            2: {
                "name": "Moderate Non-Proliferative DR",
                "description": "More than just microaneurysms but less than severe NPDR",
                "risk": "Moderate",
                "follow_up": "3-6 month follow-up",
                "color": "#e67e22"
            },
            3: {
                "name": "Severe Non-Proliferative DR",
                "description": "Any of the following with no signs of PDR: 20+ intraretinal hemorrhages, venous beading, IRMA",
                "risk": "High",
                "follow_up": "Prompt referral to ophthalmologist",
                "color": "#e74c3c"
            },
            4: {
                "name": "Proliferative DR",
                "description": "Neovascularization and/or vitreous/preretinal hemorrhage",
                "risk": "Very High",
                "follow_up": "Immediate treatment required",
                "color": "#c0392b"
            }
        }

        self.treatment_options = {
            "Mild": ["Blood sugar control", "Annual eye exams", "Lifestyle modifications"],
            "Moderate": ["Laser photocoagulation", "Anti-VEGF injections", "Frequent monitoring"],
            "Severe": ["Pan-retinal photocoagulation", "Anti-VEGF therapy", "Surgical consultation"],
            "PDR": ["Vitrectomy", "Retinal laser", "Intravitreal injections", "Regular follow-ups"]
        }

    def generate_comprehensive_analysis(self, image):
        """Generate detailed mock analysis with enhanced features"""
        width, height = image.size

        # Enhanced feature detection simulation
        features = {
            "microaneurysms": {
                "count": random.randint(0, 60),
                "density": random.uniform(0, 1),
                "locations": self.generate_random_locations(10, width, height)
            },
            "hemorrhages": {
                "count": random.randint(0, 35),
                "size_variance": random.uniform(0.1, 2.0),
                "locations": self.generate_random_locations(8, width, height)
            },
            "exudates": {
                "count": random.randint(0, 45),
                "intensity": random.uniform(0, 1),
                "macular_involvement": random.choice([True, False]),
                "locations": self.generate_random_locations(12, width, height)
            },
            "cotton_wool_spots": {
                "count": random.randint(0, 15),
                "distribution": random.choice(["focal", "scattered", "clustered"]),
                "locations": self.generate_random_locations(6, width, height)
            }
        }

        severity_score = self.calculate_enhanced_severity(features)
        risk_assessment = self.assess_comprehensive_risk(features, severity_score)

        return {
            "features": features,
            "severity_score": severity_score,
            "stage_info": self.stages[severity_score],
            "risk_assessment": risk_assessment,
            "confidence": random.uniform(0.88, 0.99),
            "processing_time": random.uniform(1.5, 3.5),
            "image_quality": self.assess_image_quality(image),
            "recommendations": self.generate_comprehensive_recommendations(severity_score, features),
            "progression_risk": self.calculate_progression_risk(severity_score, features)
        }

    def generate_random_locations(self, count, width, height):
        """Generate random locations for retinal features"""
        return [(random.randint(50, width - 50), random.randint(50, height - 50))
                for _ in range(count)]

    def calculate_enhanced_severity(self, features):
        """Calculate enhanced severity score with weighted factors"""
        score = 0

        # Weighted scoring
        weights = {
            "microaneurysms": 0.2,
            "hemorrhages": 0.3,
            "exudates": 0.25,
            "cotton_wool_spots": 0.25
        }

        ma_score = min(features["microaneurysms"]["count"] / 15, 1) * weights["microaneurysms"]
        he_score = min(features["hemorrhages"]["count"] / 10, 1) * weights["hemorrhages"]
        ex_score = min(features["exudates"]["count"] / 12, 1) * weights["exudates"]
        cws_score = min(features["cotton_wool_spots"]["count"] / 5, 1) * weights["cotton_wool_spots"]

        total_score = (ma_score + he_score + ex_score + cws_score) * 4

        return min(int(total_score), 4)

    def assess_comprehensive_risk(self, features, severity):
        """Comprehensive risk assessment"""
        risks = []

        if features["microaneurysms"]["count"] > 25:
            risks.append({"type": "High microaneurysm density", "level": "moderate"})

        if features["hemorrhages"]["count"] > 15:
            risks.append({"type": "Multiple hemorrhages", "level": "high"})

        if features["exudates"]["macular_involvement"]:
            risks.append({"type": "Macular edema risk", "level": "high"})

        if features["cotton_wool_spots"]["count"] > 8:
            risks.append({"type": "Significant ischemia", "level": "high"})

        if severity >= 3:
            risks.append({"type": "Advanced disease stage", "level": "very high"})

        return risks if risks else [{"type": "Low risk profile", "level": "low"}]

    def assess_image_quality(self, image):
        """Mock image quality assessment"""
        quality_factors = {
            "focus": random.uniform(0.7, 0.98),
            "illumination": random.uniform(0.6, 0.95),
            "contrast": random.uniform(0.5, 0.9),
            "artifact_level": random.uniform(0.1, 0.4)
        }

        overall_quality = (quality_factors["focus"] + quality_factors["illumination"] +
                           quality_factors["contrast"] + (1 - quality_factors["artifact_level"])) / 4

        return {
            "score": overall_quality,
            "factors": quality_factors,
            "grade": "Excellent" if overall_quality > 0.8 else "Good" if overall_quality > 0.6 else "Acceptable"
        }

    def calculate_progression_risk(self, severity, features):
        """Calculate risk of progression to next stage"""
        base_risk = [0.05, 0.15, 0.35, 0.65, 0.85][severity]

        # Adjust based on features
        feature_modifier = (
                features["microaneurysms"]["count"] * 0.002 +
                features["hemorrhages"]["count"] * 0.005 +
                features["exudates"]["count"] * 0.003 +
                features["cotton_wool_spots"]["count"] * 0.01
        )

        return min(base_risk + feature_modifier, 0.95)

    def generate_comprehensive_recommendations(self, severity, features):
        """Generate detailed recommendations"""
        recommendations = []

        # Stage-based recommendations
        stage_recs = {
            0: ["Continue annual screening", "Maintain optimal glucose control"],
            1: ["6-12 month follow-up", "Tighten glucose control", "Monitor blood pressure"],
            2: ["3-6 month follow-up", "Consider ophthalmology referral", "Aggressive risk factor management"],
            3: ["Immediate ophthalmology consultation", "Laser treatment evaluation", "Frequent monitoring"],
            4: ["Urgent treatment initiation", "Surgical evaluation", "Close follow-up care"]
        }

        recommendations.extend(stage_recs[severity])

        # Feature-specific recommendations
        if features["exudates"]["macular_involvement"]:
            recommendations.append("Macular edema assessment required")

        if features["hemorrhages"]["count"] > 20:
            recommendations.append("Consider anti-VEGF therapy evaluation")

        return recommendations

    def create_enhanced_severity_gauge(self, severity_score):
        """Create enhanced severity gauge with stage information"""
        stage_info = self.stages[severity_score]

        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=severity_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={
                'text': f"DR Severity: {stage_info['name']}",
                'font': {'size': 20}
            },
            delta={'reference': 0},
            gauge={
                'axis': {'range': [None, 4], 'tickwidth': 1},
                'bar': {'color': stage_info['color']},
                'steps': [
                    {'range': [0, 1], 'color': 'lightgreen'},
                    {'range': [1, 2], 'color': 'yellow'},
                    {'range': [2, 3], 'color': 'orange'},
                    {'range': [3, 4], 'color': 'red'}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': severity_score
                }
            }
        ))

        fig.update_layout(
            height=350,
            margin=dict(l=50, r=50, t=100, b=50)
        )

        return fig


def generate_sample_patients(count=50):
    """Generate comprehensive sample patient data"""
    patients = []

    for i in range(count):
        age = random.randint(25, 80)
        diabetes_duration = random.randint(1, 30)
        hba1c = round(random.uniform(5.5, 12.0), 1)
        bp_systolic = random.randint(110, 180)
        bp_diastolic = random.randint(70, 110)

        # Calculate DR stage based on risk factors
        base_risk = (age / 80 * 0.2 +
                     min(diabetes_duration / 30, 1) * 0.3 +
                     min((hba1c - 5.5) / 6.5, 1) * 0.3 +
                     min((bp_systolic - 110) / 70, 1) * 0.2)

        dr_stage = min(int(base_risk * 4), 4)

        patients.append({
            'patient_id': f'P{10000 + i}',
            'name': fake.name(),
            'age': age,
            'gender': random.choice(['Male', 'Female']),
            'diabetes_type': random.choice(['Type 1', 'Type 2']),
            'diabetes_duration': diabetes_duration,
            'hba1c': hba1c,
            'bp_systolic': bp_systolic,
            'bp_diastolic': bp_diastolic,
            'dr_stage': dr_stage,
            'last_screening': fake.date_between(start_date='-2y', end_date='today'),
            'next_appointment': fake.date_between(start_date='today', end_date='+6m'),
            'risk_score': round(base_risk * 100, 1)
        })

    return pd.DataFrame(patients)