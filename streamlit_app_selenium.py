# streamlit_app_selenium.py
import streamlit as st
from scraper_selenium import search_leads, save_to_csv
import pandas as pd

st.set_page_config(page_title="Lead Generation Scraper", layout="wide")
st.title("🔍 Lead Generation Scraper")

# Text input and slider for search
query = st.text_input("Enter your search keyword", "AI startup San Francisco")
num_results = st.slider("Number of results", min_value=2, max_value=7, value=5)

# Function to display email extraction
def display_emails(email_list):
    if isinstance(email_list, list):
        return ', '.join(email_list)
    return email_list

if st.button("Run Search"):
    with st.spinner("Searching for leads..."):
        results = search_leads(query, num_results)
        
        if results:
            save_to_csv(results)
            
            # Convert results into a DataFrame
            df = pd.DataFrame(results)
            # Format the email addresses to be displayed in a readable way
            df["emails"] = df["emails"].apply(display_emails)
            
            st.success("Leads fetched and saved to assets/data/leads_selenium.csv!")
            st.dataframe(df)
            
            # Add a download button for the CSV file
            st.download_button("Download CSV", df.to_csv(index=False), file_name="leads_streamlit.csv", mime="text/csv")
        else:
            st.error("No leads found for your query.")

st.markdown("---")
st.caption("Built for Caprae Capital Pre-Work Assignment")
