import streamlit as st
import pandas as pd
import os

from config import FINAL_CSV

st.set_page_config(
    page_title="Healthcare Leads",
    page_icon="🏥",
    layout="wide"
)

def load_data():
    if not os.path.exists(FINAL_CSV):
        st.error("Final CSV file not found. Please check data/healthcare_leads_final.csv")
        st.stop()

    df = pd.read_csv(FINAL_CSV)

    if "Lead Score" in df.columns:
        df["Lead Score"] = pd.to_numeric(df["Lead Score"], errors="coerce").fillna(0)

    return df

df = load_data()

st.title("🏥 Healthcare Leads Dashboard")
st.write("Healthcare lead generation dashboard for clinics, hospitals, pharmacies, dentists, and healthcare centers.")

col1, col2, col3, col4 = st.columns(4)

total_leads = len(df)

high_leads = 0
with_website = 0
with_phone = 0

if "Business Potential Category" in df.columns:
    high_leads = len(df[df["Business Potential Category"] == "High"])

if "Website Classification" in df.columns:
    with_website = len(df[df["Website Classification"].isin(["Good Website", "Poor Website"])])

if "Phone Number" in df.columns:
    with_phone = len(df[df["Phone Number"].fillna("").astype(str).str.strip() != ""])

col1.metric("Total Leads", total_leads)
col2.metric("High Potential", high_leads)
col3.metric("With Website", with_website)
col4.metric("With Phone", with_phone)

st.divider()

search_text = st.text_input("Search business or location")

filtered_df = df.copy()

if search_text:
    search_lower = search_text.lower()

    business_col = filtered_df["Business Name"].fillna("").astype(str).str.lower()
    location_col = filtered_df["Location"].fillna("").astype(str).str.lower()

    filtered_df = filtered_df[
        business_col.str.contains(search_lower, na=False) |
        location_col.str.contains(search_lower, na=False)
    ]

if "Industry Category" in filtered_df.columns:
    categories = ["All"] + sorted(filtered_df["Industry Category"].dropna().astype(str).unique().tolist())
    selected_category = st.selectbox("Category", categories)

    if selected_category != "All":
        filtered_df = filtered_df[filtered_df["Industry Category"].astype(str) == selected_category]

if "Website Classification" in filtered_df.columns:
    website_options = ["All"] + sorted(filtered_df["Website Classification"].dropna().astype(str).unique().tolist())
    selected_website = st.selectbox("Website Status", website_options)

    if selected_website != "All":
        filtered_df = filtered_df[filtered_df["Website Classification"].astype(str) == selected_website]

if "Business Potential Category" in filtered_df.columns:
    potential_options = ["All"] + sorted(filtered_df["Business Potential Category"].dropna().astype(str).unique().tolist())
    selected_potential = st.selectbox("Business Potential", potential_options)

    if selected_potential != "All":
        filtered_df = filtered_df[filtered_df["Business Potential Category"].astype(str) == selected_potential]

if "Lead Score" in filtered_df.columns:
    filtered_df = filtered_df.sort_values("Lead Score", ascending=False)

st.subheader("Lead Results")
st.write(f"Showing {len(filtered_df)} leads")

display_columns = [
    "Business Name",
    "Lead Score",
    "Industry Category",
    "Location",
    "Phone Number",
    "Email Address",
    "Website Classification",
    "Business Potential Category",
    "Website URL",
    "Google Maps Profile Link",
    "Reason for Classification"
]

available_columns = [col for col in display_columns if col in filtered_df.columns]

st.dataframe(
    filtered_df[available_columns],
    use_container_width=True,
    height=500
)

csv_data = filtered_df.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    "Download Filtered Leads",
    data=csv_data,
    file_name="filtered_healthcare_leads.csv",
    mime="text/csv"
)

import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, "data")

RAW_OSM_CSV = os.path.join(DATA_DIR, "healthcare_osm_raw.csv")
ONLINE_PRESENCE_CSV = os.path.join(DATA_DIR, "healthcare_online_presence.csv")
WEBSITE_ANALYSIS_CSV = os.path.join(DATA_DIR, "healthcare_website_analysis.csv")
SCORED_LEADS_CSV = os.path.join(DATA_DIR, "healthcare_scored_leads.csv")
CONTACT_ENRICHED_CSV = os.path.join(DATA_DIR, "healthcare_contact_enriched.csv")
FINAL_CSV = os.path.join(DATA_DIR, "healthcare_leads_final.csv")
