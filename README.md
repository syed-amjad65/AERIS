# ✈️ AERIS™ - Aviation Enterprise Resource Intelligence Suite

**Manager Resource Planning & Analysis Dashboard**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 Role Alignment: Manager Resource Planning & Analysis

This dashboard demonstrates **every competency** required for the Riyadh Air role:

| Competency | Implementation |
|------------|----------------|
| Strategic workforce planning | ST/MT/LT forecasting models |
| Demand forecasting | Prophet + Random Forest |
| Resource optimization | Linear programming (PuLP) |
| Regulatory compliance | EASA, FAA, GACA, GCAA rules |
| Fatigue Risk Management | FRMS scoring system |
| Executive dashboards | Streamlit interactive UI |

---

## 📊 Dashboard Features (Text Preview)
┌─────────────────────────────────────────────────────────────┐
│ EXECUTIVE OVERVIEW │
├─────────────────────────────────────────────────────────────┤
│ Total Flight Crew: 245 Total Cabin Crew: 1,200 │
│ Aircraft in Fleet: 78 EASA Compliance: 94% │
├─────────────────────────────────────────────────────────────┤
│ │
│ 👨‍✈️ Flight Crew Page: │
│ - Rank distribution (Captain/FO/Senior FO) │
│ - EASA/FAA/GACA compliance flags │
│ - Fatigue score monitoring │
│ │
│ 🛩️ Fleet Page: │
│ - A320: 20 aircraft │
│ - A350: 15 aircraft │
│ - A380: 5 aircraft │
│ - B777: 12 aircraft │
│ - B777ER: 8 aircraft │
│ - B787: 18 aircraft │
│ │
│ ⚠️ Fatigue Risk Page: │
│ - Real-time fatigue scores │
│ - FRMS Protocol alerts │
│ - Mandatory rest recommendations │
│ │
└─────────────────────────────────────────────────────────────┘

text

---

## 🚀 Live Dashboard

**To view the interactive dashboard:**

### Option 1: Run Locally (2 minutes)
```bash
git clone https://github.com/syed-amjad65/AERIS.git
cd AERIS
pip install -r requirements.txt
streamlit run ui/app.py

