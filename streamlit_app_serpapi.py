import streamlit as st
import pandas as pd
from scraper_serpapi import search_leads_serpapi, save_to_csv

st.set_page_config(page_title="Lead Scraper with SerpAPI", layout="wide")
st.title("🔍 Lead Generation Scraper (SerpAPI)")

query = st.text_input("Enter your search keyword", "AI startup San Francisco")
num_results = st.slider("Number of results", min_value=3, max_value=10, value=5)

if st.button("Run SerpAPI Search"):
    with st.spinner("Searching for leads using SerpAPI..."):
        try:
            results = search_leads_serpapi(query, num_results)
            save_to_csv(results)
            df = pd.DataFrame(results)
            df["emails"] = df["emails"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
            st.success("Leads fetched and saved to leads_serpapi.csv!")
            st.dataframe(df)
            st.download_button(
                label="Download CSV",
                data=df.to_csv(index=False),
                file_name="leads_serpapi.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")
st.caption("Built for Caprae Capital Pre-Work Assignment using SerpAPI")
