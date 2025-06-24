import streamlit as st
import pandas as pd
from analysis.data_cleaning import load_and_clean_data
from analysis.eda import get_kpis, get_sales_by_category
from visuals.charts import line_chart_sales_trend, bar_chart_top_products

st.title("📊 Sales Data Analysis Dashboard")

file_path = "data/sales_data.csv"
df = load_and_clean_data(file_path)

region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())

df_filtered = df[df['Region'].isin(region) & df['Category'].isin(category)]

kpis = get_kpis(df_filtered)
st.metric("Total Sales", f"${kpis['Total Sales']:.2f}")
st.metric("Total Profit", f"${kpis['Total Profit']:.2f}")
st.metric("Total Quantity", f"{int(kpis['Total Quantity'])}")
st.metric("Average Discount", f"{kpis['Average Discount']:.2%}")

st.plotly_chart(line_chart_sales_trend(df_filtered))
st.plotly_chart(bar_chart_top_products(df_filtered))