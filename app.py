import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit setup
st.title("Stock Valuation and Financial Analysis Tool")

# Define the list of stocks
list_of_stocks = ['786', 'AABS', 'AAL', 'AASM', 'AATM', 'ABL', 'ABOT', 'ABSON', 'ACPL', 'ADAMS', 'ADMM', 'AGHA', 
                  'AGIC', 'AGIL', 'AGL', 'AGLNCPS', 'AGP', 'AGSML', 'AGTL', 'AHCL', 'AHL', 'AHTM', 'AICL', 'AIRLINK', 
                  'AKBL', 'AKDHL', 'AKDSL', 'AKGL', 'ALAC', 'ALIFE', 'ALNRS', 'ALTN', 'AMBL', 'AMSL', 'AMTEX', 'ANL', 
                  # Add more symbols as needed
                  'PSX']

# Streamlit dropdown for stock selection
stock_symbol = st.selectbox("Select a stock symbol:", options=list_of_stocks)

# Function to fetch financial data
def get_financial_data(stock_symbol):
    urls = {
        "income_statement": f"https://stockanalysis.com/quote/{stock_symbol}/financials/",
        "balance_sheet": f"https://stockanalysis.com/quote/{stock_symbol}/financials/balance-sheet/",
        "cash_flow": f"https://stockanalysis.com/quote/{stock_symbol}/financials/cash-flow-statement/",
        "ratios": f"https://stockanalysis.com/quote/{stock_symbol}/financials/ratios/"
    }
    data = {}
    for key, url in urls.items():
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            response = requests.get(url, headers=headers)
            data[key] = pd.read_html(response.text)[0]
            data[key].columns = data[key].columns.droplevel(1)
            data[key] = data[key].T
            data[key].columns = data[key].iloc[0]
            data[key] = data[key][1:]
            data[key].replace('-', '0', inplace=True)
            data[key] = data[key].replace('%', '', regex=True)
            data[key] = data[key].astype(float)
            data[key]['Year'] = ['TTM', '2024', '2023', '2022', '2021', '2020']
        except Exception as e:
            st.error(f"Error retrieving data from {url}: {e}")
    return data

# Plotting function
def plot_dataframe(data):
    income_metrics = ['Revenue', 'Revenue Growth (YoY) (%)', 'Gross Margin (%)', 'Operating Margin (%)', 'Profit Margin (%)', 'Interest Expense']
    balance_metrics = ['Cash & Equivalents', 'Property, Plant & Equipment', 'Long-Term Debt', 'Retained Earnings', 'Book Value Per Share']
    cash_metrics = ['Free Cash Flow', 'Free Cash Flow Per Share']
    ratio_metrics = ['Debt / Equity Ratio', 'Current Ratio', 'Return on Equity (ROE) (%)', 'Return on Assets (ROA) (%)', 'Return on Capital (ROIC) (%)']

    for key, df in data.items():
        if st.checkbox(f"Show plots for {key.replace('_', ' ').title()}"):
            st.write(f"Available columns in {key}: {', '.join(df.columns)}")
            if key == 'income_statement':
                for metric in income_metrics:
                    if metric in df.columns:
                        st.bar_chart(df.set_index('Year')[metric])
            elif key == 'balance_sheet':
                for metric in balance_metrics:
                    if metric in df.columns:
                        st.bar_chart(df.set_index('Year')[metric])
            elif key == 'cash_flow':
                for metric in cash_metrics:
                    if metric in df.columns:
                        st.bar_chart(df.set_index('Year')[metric])
            elif key == 'ratios':
                for metric in ratio_metrics:
                    if metric in df.columns:
                        st.bar_chart(df.set_index('Year')[metric])

# Streamlit sidebar for valuation method selection
st.sidebar.header("Valuation Method")
method = st.sidebar.radio("Select Valuation Method:", options=["Gordon Growth Model (GGM)", "Discounted Cash Flow (DCF)", "PEG Ratio"])

# User inputs for valuation
if method == "Gordon Growth Model (GGM)":
    st.sidebar.subheader("Gordon Growth Model (GGM) Inputs")
    dividend = st.sidebar.number_input("Expected dividend next year (PKR):", min_value=0.0, step=0.1)
    growth_rate_ggm = st.sidebar.number_input("Dividend growth rate (%):", min_value=0.0, step=0.1) / 100
    required_rate = st.sidebar.number_input("Required rate of return (%):", min_value=0.1, step=0.1) / 100

    # Display GGM valuation result
    if st.sidebar.button("Calculate GGM"):
        if required_rate <= growth_rate_ggm:
            st.sidebar.error("Required return must be greater than the growth rate.")
        else:
            ggm_valuation = dividend / (required_rate - growth_rate_ggm)
            st.sidebar.success(f"GGM Valuation: PKR {ggm_valuation:,.2f}")

elif method == "Discounted Cash Flow (DCF)":
    st.sidebar.subheader("Discounted Cash Flow (DCF) Inputs")
    recent_free_cash_flow = st.sidebar.number_input("Most recent free cash flow (PKR):", min_value=0.0, step=1000.0)
    growth_rate_dcf = st.sidebar.number_input("Free cash flow growth rate (%):", min_value=0.0, step=0.1) / 100
    discount_rate_dcf = st.sidebar.number_input("Discount rate (%):", min_value=0.0, step=0.1) / 100

    # Display DCF valuation result
    if st.sidebar.button("Calculate DCF"):
        projected_cash_flows = []
        for year in range(1, 6):
            future_cash_flow = recent_free_cash_flow * ((1 + growth_rate_dcf) ** year)
            present_value = future_cash_flow / ((1 + discount_rate_dcf) ** year)
            projected_cash_flows.append(present_value)
        dcf_valuation = sum(projected_cash_flows)
        st.sidebar.success(f"DCF Valuation: PKR {dcf_valuation:,.2f}")

elif method == "PEG Ratio":
    st.sidebar.subheader("PEG Ratio Inputs")
    pe_ratio = st.sidebar.number_input("P/E Ratio:", min_value=0.0, step=0.1)
    growth_rate_peg = st.sidebar.number_input("Growth rate (%):", min_value=0.0, step=0.1)

    # Display PEG ratio result
    if st.sidebar.button("Calculate PEG"):
        if growth_rate_peg == 0:
            st.sidebar.error("Growth rate cannot be zero.")
        else:
            peg = pe_ratio / growth_rate_peg
            st.sidebar.success(f"PEG Ratio: {peg:.2f}")

# Fetch and display data
if stock_symbol:
    st.subheader(f"Financial Data for {stock_symbol}")
    data = get_financial_data(stock_symbol)
    if data:
        plot_dataframe(data)
