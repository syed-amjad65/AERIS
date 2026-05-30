"""
AERIS - Main Dashboard
Aviation Enterprise Resource Intelligence Suite
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="AERIS", page_icon="✈️", layout="wide")

st.title("✈️ AERIS™")
st.caption("Aviation Enterprise Resource Intelligence Suite")
st.caption("Manager Resource Planning & Analysis Dashboard")

# Generate sample data
np.random.seed(42)
flight_crew = pd.DataFrame({
    'pilot_id': [f'PL{i:04d}' for i in range(1, 101)],
    'rank': np.random.choice(['Captain', 'First Officer'], 100, p=[0.4, 0.6]),
    'hours_30d': np.random.randint(20, 100, 100),
    'hours_7d': np.random.randint(5, 35, 100),
})

st.sidebar.image("https://img.icons8.com/fluency/96/airport.png", width=80)
st.sidebar.markdown("## AERIS Control Panel")

page = st.sidebar.selectbox(
    "Select Dashboard",
    ["📊 Executive Overview", "👨‍✈️ Flight Crew", "🛩️ Fleet", "⚠️ Fatigue Risk"]
)

if page == "📊 Executive Overview":
    st.header("Executive Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Flight Crew", "245", "Active")
    with col2: st.metric("Total Cabin Crew", "1,200", "+12")
    with col3: st.metric("Aircraft in Fleet", "78", "6 types")
    with col4: st.metric("EASA Compliance", "94%", "⬆️")
    
    rank_counts = flight_crew['rank'].value_counts()
    fig = px.pie(values=rank_counts.values, names=rank_counts.index, title="Crew Rank Distribution")
    st.plotly_chart(fig, use_container_width=True)

elif page == "👨‍✈️ Flight Crew":
    st.header("Flight Crew Management")
    compliant = (flight_crew['hours_30d'] <= 100).sum()
    st.metric("EASA Compliant Crew", f"{compliant}/{len(flight_crew)}")
    fig = px.histogram(flight_crew, x='hours_7d', title="Weekly Flight Hours")
    st.plotly_chart(fig, use_container_width=True)

elif page == "🛩️ Fleet":
    st.header("Fleet Management")
    fleet_data = pd.DataFrame({
        'Aircraft Type': ['A320', 'A350', 'A380', 'B777', 'B777ER', 'B787'],
        'Count': [20, 15, 5, 12, 8, 18]
    })
    fig = px.bar(fleet_data, x='Aircraft Type', y='Count', title="Fleet Composition")
    st.plotly_chart(fig, use_container_width=True)

elif page == "⚠️ Fatigue Risk":
    st.header("Fatigue Risk Management")
    flight_crew['fatigue_score'] = flight_crew['hours_7d'] / 60
    high_risk = (flight_crew['fatigue_score'] > 0.7).sum()
    st.metric("High Risk Crew", high_risk)
    st.info("Score >0.7 → 12h rest | Score >0.8 → 24h rest")

st.markdown("---")
st.markdown("AERIS™ v1.0 | EASA Compliant | FAA Part 117 | GACA Part 4")
