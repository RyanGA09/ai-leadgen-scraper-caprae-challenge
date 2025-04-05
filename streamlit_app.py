# streamlit_app.py
import streamlit as st
from scraper_selenium import search_leads, save_to_csv
import pandas as pd

st.set_page_config(page_title="Lead Generation Scraper", layout="wide")
st.title("🔍 Lead Generation Scraper")

query = st.text_input("Enter your search keyword", "AI startup San Francisco")
num_results = st.slider("Number of results", min_value=3, max_value=10, value=5)

if st.button("Run Search"):
    with st.spinner("Searching for leads..."):
        results = search_leads(query, num_results)
        save_to_csv(results)
        df = pd.DataFrame(results)
        df["emails"] = df["emails"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
        st.success("Leads fetched and saved to leads.csv!")
        st.dataframe(df)
        st.download_button("Download CSV", df.to_csv(index=False), file_name="leads_streamlit.csv", mime="text/csv")

st.markdown("---")
st.caption("Built for Caprae Capital Pre-Work Assignment")